#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<unordered_map>
#include<queue>
#include<stack>
#include<iterator>
#include<cmath>
#include<string>
#include<sstream>
#include<cstring>
#include<ctype.h>
#include<iomanip>
#include<bitset>
#include<stdio.h>
#include<fstream>
#include<regex>
#include<stdlib.h>
#include<math.h>

using namespace std;

#define all(v)         v.begin(),v.end()
#define sz(V)        ((int)((v).size()))
#define psh(x)               push_back(x)
#define mk(x,y)           make_pair(x,y)
#define ck(a)               (a<1 || a>9)
#define lop(i,n)     for(ll i=0;i<n;i++)
#define loop(i,f,l)  for(ll i=f;i<l;i++)
#define READ(s)   freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
#define scl(n)          scanf("%lld",&n)
#define sc(n)             scanf("%d",&n)
#define INF                   1000000000
#define PI             3.141592653589793

typedef string            ss;
typedef long long         ll;
typedef pair <int, int>   ii;
typedef pair<string, int> si;
typedef pair<int, string> is;
typedef pair<char, int>  chi;
typedef vector<ii>       vii;
typedef vector<int>       vi;
typedef vector<vi>       vvi;
typedef vector<string>    vs;
typedef vector<ll>       vll;
typedef vector<vii>     vvii;

int gcd(int a, int b) { return (b == 0 ? a : gcd(b, a % b)); }
int lcm(int a, int b) { return ((a*b) / gcd(a, b)); }
ll pw(ll b, ll p){ if (!p) return 1; ll sq = pw(b, p / 2); sq *= sq; if (p % 2) sq *= b; return sq; }
int sd(ll x){ return x<10 ? x : x % 10 + sd(x / 10); }
ll sq(ll x){ lop(i, x)if ((ll)i*i > x) return (i - 1); return ll(1); }
//READ("input.txt");WRITE("output.txt");
//#include <bits/stdc++.h>
//using namespace std;

ll T, s, n, r;
ss str;

int main()
{
	READ("A-large.txt");WRITE("output.txt");
	scl(T);
	for (int i = 1; i <= T; i++)
	{
		scl(s); cin >> str;
		n = 0, r = 0;
		for (ll j = 0; j < str.length(); j++)
		{
			if (j <= n) n += int(str[j] - '0');
			else
			{
				r += j - n;
				n += (j - n);
				n += int(str[j] - '0');
			}
		}
		printf("Case #%d: %d\n", i, r);
	}
}