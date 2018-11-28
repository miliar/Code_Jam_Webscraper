#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<vector>
#include<string>
#include<iostream>
#include<algorithm>
#include<map>
#include<iterator>
#include<set>
#include<stack>
#include<queue>
#include<fstream>
#include<iomanip>
#include<list>
#include <sstream>
#include<cmath>
#include<math.h>
#define rep(i,m,n) for(int i = (m); i < (n); i++)
#define repd(i,m,n) for(int i=(m); i > (n); i--)
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define mp make_pair
#define endl '\n'
//#define x first
//#define y second
//#define b first
//#define e second
#define row first
#define col second
using namespace std;
const ll MAX = (ll)1000*1000*1000;
int t,n,j;
ll npow[11][17];
int isNotPrime(ll num)
{
	ll to = sqrt(num) + 2;
	rep(i,2,to)
		if (num % i == 0)
			return i;
	return 0;
}
vector<ll> res;

bool approve(ll num)
{
	res.clear();
	rep(i,2,11)
	{
		ll temp = npow[i][n-1] + 1;

		rep(k,0,n-3)
			if (num & (1 << k))
				temp += npow[i][k+1];
		ll vid = isNotPrime(temp);
		if (vid)
		{
			res.push_back(vid);
			if (i == 10)
				return true;
		}else
			break;
	}

	return false;
}

void print(ll num)
{
	cout << 1;
	repd(i,n-3,-1)
		cout << ((num & (1 << i)) ? 1 : 0);
	cout << 1;
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
	freopen("input.in", "rt", stdin);
	freopen("output.out", "wt", stdout);
	//t = 1; n = 16; j = 50;
	cin >> t >> n >> j;
	rep(i,0,11)
		npow[i][0] = 1;
	rep(i,0,11)
		rep(j1,1,17)
		npow[i][j1] = npow[i][j1-1]*i;
	
	cout << "Case #1:" << endl;
    ll j1 = j;
	rep(i,0, 1 << (n - 2) )
	{
		if (approve(i))
		{
			//cout << j << endl;
			print(i);
			cout << " ";
			rep(k,0,res.size())
				cout << res[k] << " ";
			cout << endl;
			j1--;
		}
		if (!j1)
			return 0;
	}
	return 0;
}

