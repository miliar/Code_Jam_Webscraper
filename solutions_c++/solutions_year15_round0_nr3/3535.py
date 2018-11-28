#include <iostream>
#include <string>
#include <thread>

using namespace std;

enum qdi
{
	_1,
	_i,
	_j,
	_k,
	_m1,
	_mi,
	_mj,
	_mk,

	cnt
};
const qdi mt[cnt][cnt] = {
	{ _1, _i, _j, _k, _m1, _mi, _mj, _mk },
	{ _i, _m1, _k, _mj, _mi, _1, _mk, _j },
	{ _j, _mk, _m1, _i, _mj, _k, _1, _mi },
	{ _k, _j, _mi, _m1, _mk, _mj, _i, _1 },
	{ _m1, _mi, _mj, _mk, _1, _i, _j, _k },
	{ _mi, _1, _mk, _j, _i, _m1, _k, _mj },
	{ _mj, _k, _1, _mi, _j, _mk, _m1, _i },
	{ _mk, _mj, _i, _1, _k, _j, _mi, _m1 } };
qdi operator*(qdi x, qdi y)
{
	return mt[x][y];
}
qdi operator*=(qdi& x, qdi y)
{
	x = x * y;
	return x;
}
qdi ctqi(char c)
{
	switch (c)
	{
	case 'i':	return _i;
	case 'j':	return _j;
	case 'k':	return _k;
	default:	return _1;
	}
}
bool canReduce(string str, int X)
{
	const int srs = (int)str.size();
	const int sts = srs * X;
	qdi valI = _1;
	for (int x = 0; x < sts; x++)
	{
		valI *= ctqi(str[x % srs]);
		if (valI == _i)
		{
			qdi valJ = _1;
			for (int y = x + 1; y < sts; y++)
			{
				valJ *= ctqi(str[y % srs]);
				if (valJ == _j)
				{
					qdi valK = _1;
					for (int z = y + 1; z < sts; z++)
					{
						valK *= ctqi(str[z % srs]);
						if (valK == _k && z == strTotalSize - 1)
							return true;
					}
				}
			}
		}
	}
	return false;
}

struct it
{
	int X;
	string str;

	it() : X(-1) { }
};
it ipt[100];
bool results[100];
void threadCompute(int start, int end)
{
	for (int i = start; i < end; i++)
		if (ipt[i].X > 0)
			results[i] = canReduce(ipt[i].str, ipt[i].X);
}
int main()
{
	int nbTests;
	cin >> nbTests;
	for (int testId = 0; testId < nbTests; testId++)
	{
		int L;
		cin >> L >> ipt[testId].X >> ipt[testId].str;
	}

	thread* threads[8];
	const int resultsPerThread = nbTests / 8;
	for (int i = 0; i < 8 - 1; i++)
		threads[i] = new thread(threadCompute, i * resultsPerThread, (i + 1) * resultsPerThread);
	threads[8 - 1] = new thread(threadCompute, (8 - 1) * resultsPerThread, nbTests);
	for (int i = 0; i < 8; i++)
	{
		threads[i]->join();
		delete (threads[i]);
	}

	for (int testId = 0; testId < nbTests; testId++)
		cout << "Case #" << testId + 1 << ": " << (const char*)(results[testId] ? "YES" : "NO") << endl;

	return 0;
}
