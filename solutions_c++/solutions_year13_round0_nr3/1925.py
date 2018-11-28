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
#include <assert.h>

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define PI 3.14159265358979
#define forn(i, n) for(int i = 0; i < n; ++i)
#define ALL(x) x.begin(), x.end()
#define L(s) (int)((s).size())
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

ll ABS(ll a)
{
    if(a<0)
        return a*(-1);
    else
        return a;
}


bool polin(ll k)
{
	string cur = "";
	while(k)
	{
		cur+=(k%10 + '0');
		k/=10;
	}
	int l = L(cur)-1;
	int f = 0;
	while(f <= l)
	{
		if(cur[l]!=cur[f])
			return false;
		f++;
		l--;
	}
	return true;
}

vector<ll> ch;
int main()
{
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
	int cur = 1;
	cin >> T;
	for(ll i = 1;i <= 10000000;i++)
	{
		if(polin(i))
		{
			ll d = i * i;
			if(polin(d))
			{
				ch.pb(d);
//				cout << d << " = " << i << endl;
			}
		}
	}
	while(cur<=T)
	{
		ll A,B;
		cin >> A >> B;
		int ans = 0;
		for(int i = 0;i < L(ch);i++)
		{
			if(ch[i] >= A && ch[i] <= B)
				ans++;
		}
		printf("Case #%d: %d\n",cur,ans);
		cur++;
	}

    return 0;
}