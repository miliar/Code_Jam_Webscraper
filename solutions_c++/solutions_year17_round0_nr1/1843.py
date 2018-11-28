#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <list>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <stack>

using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define FOR(i, a, n) for(int i=(a), __ ## i=(n); i<__ ## i; i++)
#define REP(I,N) FOR(I,0,N)
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
#define PRV(X) {cout<<#X<<" = {";REP(__prv,sz(X)-1)cout<<(X)[__prv]<<",";if(sz(X))cout<<*(X).end();cout<<"}"<<endl;}

template<class T> ostream &operator<<(ostream &os, const vector<T> &vec)
{
	os << '{';
	REP(i, sz(vec))
	{
		os << vec[i];
		if (i + 1 != sz(vec))
			os << ',';
	}
	os << '}';
	return os;
}

template<class T1, class T2> ostream &operator<<(ostream &os, const pair<T1, T2> &par)
{
	os << '(' << par.X << ',' << par.Y << ')';
	return os;
}

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<unsigned long long> VULL;
typedef vector<vector<int>> VVI;
typedef queue<int> QI;

int gcd(int x, int y)
{
	return y ? gcd(y, x % y) : abs(x);
}

template<class T> T sqr(T x)
{
	return x * x;
}

int main()
{
	ifstream fin("file.in");
	ofstream fout("file.out");
	ios::sync_with_stdio(false);

	int T;
	fin >> T;
	REP(t, T)
	{
		string s;
		int K;
		fin >> s >> K;
		int n = s.length();
		VI flip(n+1);

		int cnt = 0;
		int sum = 0;
		bool impos = false;
		REP(i, n)
		{
			sum += flip[i];
			if ((s[i] == '-') ^ (sum&1))
			{
				if (i > n - K)
				{
					impos = true;
					break;
				}
				else
				{
					sum++;
					flip[i + K]--;
					cnt++;
				}
			}
		}

		if (impos)
			fout << "Case #" << (t + 1) << ": IMPOSSIBLE\n";
		else
			fout << "Case #" << (t + 1) << ": " << cnt << endl;
	}

	fin.close();
	fout.close();

	return 0;
}