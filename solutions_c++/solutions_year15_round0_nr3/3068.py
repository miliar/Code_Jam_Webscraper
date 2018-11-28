#include <iostream>
#include <map>
#include <future>
#include <vector>

using namespace std;

bool solve(char* we, long long L, long long X, long long pos, char cur, char* ijk, bool positive, 
	map<long long, map<char, map<char*, map<bool, bool>>>>& cache)
{
	if (cache[pos][cur][ijk].find(positive) != cache[pos][cur][ijk].end())
		return cache[pos][cur][ijk][positive];
	auto& ret = cache[pos][cur][ijk][positive];
	if (*ijk == 0 && pos == L*X+1 && positive) return ret=true;
	if (*ijk == 0 || pos == L*X + 1) return ret = false;
	if (cur == *ijk && solve(we, L, X, pos + 1, we[pos % L], ijk + 1, positive, cache))
	{
		return ret = true;
	}
	while (pos < L*X)
	{
		char n = we[pos % L];
		if (cur == '1') cur = n;
		else if (cur == 'i')
		{
			if (n == 'i') { cur = '1'; positive = !positive; }
			else if (n == 'j') { cur = 'k'; }
			else if (n == 'k') { cur = 'j'; positive = !positive; }
		}
		else if (cur == 'j')
		{
			if (n == 'i') { cur = 'k'; positive = !positive; }
			else if (n == 'j') { cur = '1'; positive = !positive; }
			else if (n == 'k') { cur = 'i'; }
		}
		else if (cur == 'k')
		{
			if (n == 'i') { cur = 'j'; }
			else if (n == 'j') { cur = 'i'; positive = !positive; }
			else if (n == 'k') { cur = '1'; positive = !positive; }
		}
		++pos;
		if (cur == *ijk && solve(we, L, X, pos + 1, we[pos % L], ijk + 1, positive, cache))
		{
			return ret = true;
		}
	}
	return ret = false;
}

int main()
{
	long long T, L, X;
	char* ijk = "ijk";
	cin >> T;
	vector<future<bool>> f;
	for (int q = 1; q <= T; ++q)
	{
		cin >> L >> X;
		char* we = new char[10002];
		we[L] = 0;
		for (int i = 0; i < L; ++i)
			cin >> we[i];
		f.push_back(async([=]{
			map<long long, map<char, map<char*, map<bool, bool>>>> cache;
			bool ret = solve(we, L, X, 1, we[0], ijk, true, cache);
			cerr << "Done " << q << endl;
			return ret;
		}));
	}
	for (int q = 1; q <= T; ++q)
	{
		cout << "Case #" << q << ": " << (f[q-1].get() ? "YES" : "NO") << endl;
	}
	return 0;
}