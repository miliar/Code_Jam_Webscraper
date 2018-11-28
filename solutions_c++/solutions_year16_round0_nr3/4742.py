#include <stack>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <math.h>
#include <vector>
#include <string.h>
#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <iostream>  
#include <string>
#include <iomanip>
#include <ctime>
using namespace std;

#define EPS 1e-9
#define ABS(a) ( (a) < 0 ? -(a) : (a) )

const double PI = 4 * atan(1.0);
const int MAXN  = (int)(210);

typedef long long ll;
const ll INF = (int)1E9 + 10;
const int MOD = (int)(1001017);
const int P = 31;

#define mp make_pair 
#define FOR(i,s,f) for(int i=s; i<f; i++)

//  prime -> 1001017
//int dir[2][4] = {{ -1, 0, 1, 0 }, { 0, 1, 0, -1 }}; 
//************************************************

ll pows[11][20];
ll del[11];

ll getNum(ll mask, ll d, ll n)
{
	ll res = 0;
	for(ll i=n-1; i >=0; i--)
	{
		if( mask&(1<<i) ) res += pows[d][i];
	}

	return res;
}

ll getD(ll n)
{
	for(ll i=2; i*i <= n; i++)
	{
		if( n%i == 0 ) return i;
	}
	return -1;
}

bool check(ll mask, ll n)
{
	for(ll i=2; i<=10; i++)
	{
		ll num = getNum( mask, i, n);
		ll d = getD(num);

		if( d == -1 ) return false;
		else
		{
			del[i] = d;
		}
	}
	return true;
}

int main()
{
freopen("C-small-attempt1.in", "rb", stdin); 
freopen("out.txt", "wt", stdout);
//unsigned int start_time =  clock();

int t; cin >> t;

for(int i=2; i <11; i++)
{
	pows[i][0] = 1;
	for(int j=1; j < 20; j++)
	{
		pows[i][j] = pows[i][j-1]*i;
	}
}

for(int f=1; f<=t; f++)
{
	ll n, cnt; cin >> n >> cnt;
	cout << "Case #"<<t<<":\n";

	ll en = 1<<n;
	for(ll x = (1<<(n-1)); x < en && cnt; x++)
	{

		if( !(x&1) ) x++;

		/*for(int i=n-1; i>=0; i--)
			{
				int num =  x&(1 << i ) ? 1 : 0 ;
				cout << num;
			}cout << endl;*/


		if( check(x, n) )
		{
			cnt--;

			for(ll i=n-1; i>=0; i--)
			{
				cout <<  ( (x&(1<<i)) ? 1 : 0 );
			}

			for(int i=2; i<=10; i++) cout <<" "<<del[i];
			cout <<  endl;
		}
	}

}

	return 0;
}

