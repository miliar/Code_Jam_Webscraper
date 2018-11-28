#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iomanip>
#include <iostream>
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

typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

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
	//    if (!freopen("1.in", "r", stdin))
	//    {
	//        cerr << "No input file" << endl;
	//        return 1;
	//    }
	//    if (!freopen("1.out", "w", stdout))
	//    {
	//        cerr << "Error creating output file" << endl;
	//        return 1;
	//    }
	ios::sync_with_stdio(false);


	FILE *f, *g;
	freopen_s(&f, "input.txt", "r", stdin);
	freopen_s(&g, "output.txt", "w", stdout);
	

	int t;
	cin >> t;

	for (int tr = 0; tr < t; tr++) {
		string s;
		int k;

		bool res = false;

		cin >> s;
		cin >> k;

		int ans = 0;

		for (int i = 0; i < s.length(); i++) {

			if (s[i] == '-' && i <= s.length() - k) {
				ans++;
				for (int j = i; j < i + k; j++)
					if (s[j] == '-') s[j] = '+'; else s[j] = '-';

			}

			else

			if (s[i] == '-' && i > s.length() - k) {
				cout << "Case #" << tr + 1 << ": IMPOSSIBLE" << endl;
				res = true;
				break;
			}

			if (res) break;

		}
		if (res) continue;
		cout << "Case #" << tr + 1 << ": " << ans << endl;
	}

	return 0;
}