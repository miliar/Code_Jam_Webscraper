#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int getBit(long long s)
{
	int ret = 0;
	while (s >= 10)
	{
		s /= 10;
		ret++;
	}
	return ret;
}

long long power10(int n)
{
	int res = 1;
	while (--n)
	{
		res *= 10;
	}
	return res;
}

long long reverse(long long m)
{
	long long ret = 0;
	while (m >= 10)
	{
		ret += (m % 10);
		m /= 10;
		ret *= 10;
	}
	ret += m;
	return ret;
}

long long getFair(long long m, int nbit)
{
	return m * power10(nbit) + reverse(m);
}

long long bin2dec(long long m)
{
	long long ret = 0;
	int i = 1;
	while (m)
	{
		ret += (m % 2) * power10(i);
		m >>= 1;
		i++;
	}
	return ret;
}

long long getFairMiddle(long long m, int mid, int nbit)
{
	return m * power10(nbit + 2) + mid * power10(nbit + 1) + reverse(m);
}

void genAll(vector<long long>& v, int m)
{
	if (m % 2 == 0)
	{
		return;
	}
	if (m == 1)
	{
		v.push_back(1ll);
		v.push_back(4ll);
		v.push_back(9ll);
		return;
	}
	
	if (m == 3)
	{
		v.push_back(121ll);
		v.push_back(484ll);
		return;
	}
	
	if (m == 5)
	{
		v.push_back(10201ll);
		v.push_back(12321ll);
		v.push_back(14641ll);
		return;
	}
	long long dec;
	int h = ((m + 1) >> 1);
	int ii;
	if (h % 2 == 0)
	{
		int e = h >> 1;
		int start = (1 << (e - 1));
		int end = (1 << e) - 1;
		for (ii = start; ii <= end; ++ii)
		{
			dec = bin2dec(ii);
			v.push_back(getFair(dec, e));
		}
	}
	else
	{
		int e = h >> 1;
		int start = (1 << (e - 1));
		int end = (1 << e) - 1;
		int jj;
		for (ii = start; ii <= end; ++ii)
		{
			dec = bin2dec(ii);
			for (jj = 0; jj <= 2; ++jj)
			{
				if (m >= 13)
				{
					if (jj == 2)
					{
						continue;
					}
				}
				v.push_back(getFairMiddle(dec, jj, e));
			}
		}
	}
}

int main()
{
	ifstream ifs("C-small-attempt0.in");
	ofstream ofs("out.txt");
	cin.rdbuf(ifs.rdbuf());
	cout.rdbuf(ofs.rdbuf());
	int T;
	int ca;
	cin >> T;
	long long A, B;
	int res;
	int num[100] = {3, 0, 2, 0, 3};
	int ii;
	for (ii = 5; ii < 100; ++ii)
	{
		if ((ii + 1) % 2 == 0)
		{
			num[ii] = 0;
		}
		else
		{
			int e = ((ii + 2) >> 1);
			if (e % 2 == 0)
			{
				num[ii] = (1 << ((e >> 1) - 1));
			}
			else
			{
				num[ii] = 3 * (1 << ((e >> 1) - 1));
				if (ii > 13)
				{
					num[ii]--;
				}
			}
		}
	}
	vector<long long> va, vb;
	int i, j;
	for (ca = 1; ca <= T; ++ca)
	{
		res = 0;
		cin >> A >> B;
		int aB = getBit(A);
		int bB = getBit(B);
		int kk;
		for (kk = aB; kk <= bB; ++kk)
		{
			res += num[kk];
		}
		va.clear();
		vb.clear();
		aB++;
		bB++;
		genAll(va, aB);
		genAll(vb, bB);
		sort(va.begin(), va.end());
		sort(vb.begin(), vb.end());
		// Modify
		if (aB % 2 != 0)
		{
			for (i = 0; i < va.size(); ++i)
			{
				if (A <= va[i])
				{
					break;
				}			
				res--;
			}
		}
		
		if (bB % 2 != 0)
		{
			for (i = vb.size() - 1; i >= 0; --i)
			{
				if (B >= vb[i])
				{
					break;
				}			
				res--;
			}
		}
		
		cout << "Case #" << ca << ": " << res << endl;
	}
	ofs.close();
	ifs.close();
	return 0;
}
