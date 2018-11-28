#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <set>
#include <cstring>
#include <limits.h>

#define inp(x) scanf("%d",&x)
#define inp_l(x) scanf("%lld",&x)
#define inp_d(x) scanf("%lf",&x)
#define MOD 1000000007

using namespace std;

typedef long long int ll;
typedef vector <int> VI;
typedef vector <long long int> VLL;
typedef pair<int,int> PI;
typedef pair<ll,ll> PLL;

int arr[10];
int x;

void fill(ll n)
{
	ll n1 = n;
	while ( n1!= 0)
	{
		ll p = n1 % 10;
		if(arr[p] == 0)
		{
			arr[p] = 1;
			x++;
		}
		n1/=10ll;
	}
}

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	int t,i,j,k,l;
	ll n,n1;
	
	cin >> t;
	for(int z = 1; z <= t; z++)
	{
		cin >> n;
		if( n == 0)
		{
			cout << "Case #" << z << ": INSOMNIA" << endl;
			continue;
		}
		for ( i = 0; i < 10; i++)
			arr[i] = 0;
		x = 0;
		n1 = n;
		while(true)
		{
			fill(n);
			//cout << x << endl;
			if(x==10)
				break;
			n += n1;
		}
		cout << "Case #" << z << ": " << n << endl;
	}
	return 0;
}

