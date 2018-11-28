#define _CRT_SECURE_NO_DEPRECATE
#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>
#include <list>
#include <fstream>

using namespace std;

#define all(v)              ((v).begin()), ((v).end())
#define allr(v)             ((v).rbegin()), ((v).rend())
#define sz(v)               ((int)((v).size()))
#define clr(v, d)           memset(v, d, sizeof(v))
#define MP                  make_pair
#define lpv(i, v)           for(int i=0;i<sz(v);++i)
#define lpn(i, n)           for(int i=0;i<(int)(n);++i)
#define V  	                vector
#define ss 	                second
#define ff 	                first

typedef unsigned long long          ull;
typedef long long                   ll;
typedef long double                 LD;

ll suf(ll a){ return (a*(a + 1)) / 2; }
const ll  OO = 1e6 + 10, S = 1e9 + 7;
vector<vector<int> >adj, can;

int dx[]{1, -1, 0, 0, 1, -1, 1, -1};
int dy[]{0, 0, 1, -1, 1, -1, -1, 1};

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ll T, N , I = 1;
	cin >> T;
	while (T--){
		string s;
		cin >> s;
		char ch = '+';
		ll ans = 0;
		for (int i = int(s.size() - 1); i >= 0; i--){
			if (s[i] != ch)
				ch = s[i], ans++;
		}
		printf("Case #%I64d: %I64d\n", I, ans);
		I++;
	}
	return 0;
}
/**/