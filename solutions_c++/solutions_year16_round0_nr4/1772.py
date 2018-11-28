#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <string>
#include <set>
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

int main()
{
	ios_base::sync_with_stdio(false); cin.tie(0);
	int t,k,c,s,i;
	cin >> t;
	for(int z = 1; z <= t; z++)
	{
		cin >> k >> c >> s;
		cout << "Case #" << z << ": ";
		for(i = 1; i <= k; i++)
		{
			cout << i << " ";
		}
		cout << endl;
	}
	return 0;
}

