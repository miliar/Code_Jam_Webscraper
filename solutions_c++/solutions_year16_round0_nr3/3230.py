#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <stack>
#include <string.h>
#include <list>
#include <time.h>

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define PI 3.14159265358979
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define L(s) (int)((s).size())
#define sz(s) (int)((s).size())
#define ms(x) memset(x,0,sizeof(x))
#define ms1(x) memset(x,-1,sizeof(x))
#define del(y,x) erase(y.begin()+x)

typedef long long ll;
using namespace std;
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;
const int ST = 100010;
const int ST1 = 1000010;
const ll MOD = 1000000007;

ll ABS(ll a) {
    if(a<0)
        return a*(-1);
    else
        return a;
}

int n;
vector<string> mms;
vector<vector<ll> > vals;


vector<int> pr;
const ll MAXN = 100000;
vector<bool> prime(MAXN,true);
void gen()
{
	prime[1] = false;
	for(ll i = 2;i < MAXN;i++)
	{
		if(prime[i])
		{
			for(ll j = i * i;j < MAXN;j+=i)
			{
				prime[j] = false;
			}
			pr.push_back(i);
		}
	}
}

ll to_i(string a,int sys)
{
	ll val = 0;
	for(int i = 0;i < L(a);i++)
	{
		val*=sys;
		val+=(a[i]-'0');
	}
	return val;
}
ll d_find(ll ch)
{
	for(int i = 0;i < L(pr) && pr[i] < ch;i++)
	{
		if(ch % pr[i] == 0)
		{
			return pr[i];
		}
	}
	return 0;
}

int kol = 0;
void rec(string a)
{
	if(L(mms)>=kol)
		return ;
	if(L(a)== n - 1)
	{
		a+='1';
		vector<ll> cur;
		for(int i = 2;i<=10;i++)
		{
			ll ch = to_i(a,i);
			ll d = d_find(ch);
			if(d==0)
				return ;
			cur.push_back(d);
		}
		mms.push_back(a);
		vals.push_back(cur);
	}
	else
	{
		rec(a + '0');
		rec(a + '1');
	}
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	cin >> n;
	cin >> kol;

	string val = "1";
	gen();
	rec(val);
	printf("Case #1:\n");
	for(int i = 0;i < L(mms);i++)
	{
		cout << mms[i] << " ";
		for(int j = 0;j < L(vals[i]);j++)
		{
			cout << vals[i][j];
			if(j == L(vals[i]) - 1)
			{
				cout << endl;
			}
			else
				cout << " ";
		}
	}

    return 0;
}