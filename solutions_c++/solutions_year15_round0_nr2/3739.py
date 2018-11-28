#include<map>
#include<string>
#include<cstring>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<queue>
#include<vector>
#include<iostream>
#include<algorithm>
#include<bitset>
#include<climits>
#include<list>
#include<iomanip>
#include<stack>
#include<set>
using namespace std;
int a[1010];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for(int cs=1;cs<=T;cs++)
	{
		int n;
		cin>>n;
		int mx=-1;
		for(int i=0;i<n;i++)
		{
			cin>>a[i];
			mx=max(mx,a[i]);
		}
		int ans=mx;
		for(int i=1;i<mx;i++)
		{
			int t=i;
			for(int j=0;j<n&&t<ans;j++)
				if(a[j]>i)
				{
					t+=a[j]/i;
					if(a[j]%i==0)
						t--;
				}
			ans=min(t,ans);
		}
		printf("Case #%d: %d\n",cs,ans);
	}
}
