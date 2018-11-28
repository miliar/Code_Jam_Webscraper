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

int arr[1001];

#define NAME "B-small-attempt13"


int main()
{
	ios::sync_with_stdio(false);
	freopen(NAME".in","r",stdin);
	freopen(NAME".out","w",stdout);
	
	int temp[1001];

	int T;
	cin >> T;
	int num = 1;
	while(T--)
	{
		cout << "Case #" << num << ": ";// << endl;
		
		int n;
		cin >> n; 
		int ans = 1000000000;
		for(int i=1;i<=n;++i)
		{
			cin >> arr[i];
			temp[i] = arr[i];
		}
		sort(temp+1,temp+1+n);
		do
		{
			int cur = 1;
			while(cur<n && temp[cur]<temp[cur+1])++cur;
			while(cur<n && temp[cur]>temp[cur+1])++cur;
			if(cur!=n)
				continue;
			
			map<int,int> data;
			int temp1[101];
			for(int j=1;j<=n;++j)
			{
				data[temp[j]] = j;
			}

			for(int j=1;j<=n;++j)
				temp1[j] = data[arr[j]];
			int tempo = 0;
			cur = 2;
			while(cur <= n)
			{
				int j = cur;
				while(j>1 && temp1[j]<temp1[j-1])
				{
					swap(temp1[j],temp1[j-1]);
					--j;
					++tempo;
				}
				++cur;
			}
			ans = min(tempo,ans);
		}
		while(next_permutation(temp+1,temp+1+n));

		++num;
		cout << ans << '\n';
	}

    return 0;
}