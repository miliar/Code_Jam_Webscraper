//***********************************
//********     WARNING      *********
//***    Bugs are everywhere!     ***
//***********************************

#include <iostream>
#include <list>
#include <stack>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <set>
#include <queue>
#include <functional>
#include <ctime>
#include <iomanip>
#include <iterator>

using namespace std;
#define double long double

typedef long long ll;
typedef unsigned long long ull;
const double oo = 1e30;
const ll ooo = 1ll << 62;

const int mod7 = 1000000007;
typedef pair<ll,ll> prl;

const double pi = acos(-1.);

int arr[1000001];

#define NAME "A-large"

int main()
{
	ios::sync_with_stdio(false);
	freopen(NAME".in","r",stdin);
	freopen(NAME".out","w",stdout);


	int T;
	cin >> T;
	int num = 1;
	while(T--)
	{
		cout << "Case #" << num << ": ";
		int n,x;
		cin >> n >> x; 
		for(int i=1;i<=n;++i)
			cin >> arr[i];

		sort(arr+1,arr+1+n);
		int l = 1;
		int ans = 0;
		for(int i=n;i>=l;--i)
		{
			if(i!=l && arr[i]+arr[l]<=x)
			{
				++l;
			}
			++ans;
		}
		++num;
		cout << ans << '\n';
	}

    return 0;
}