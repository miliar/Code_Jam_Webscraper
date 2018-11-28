#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <sstream>
using namespace std;

void solve()
{
	int n;
	static int a[1000];
	cin>>n;
	for(int i=0;i<n;i++)cin>>a[i];
	int ans=1000;
	for(int x=1;x<=1000;x++)
	{
		int s=x;
		for(int i=0;i<n;i++)
		{
			s+=a[i]/x;
			if(a[i]%x==0)s--;
		}
		ans=min(ans,s);
	}
	cout<<ans<<endl;
}
int main()
{
	freopen("/Users/francis/Documents/in.txt","r",stdin);
	freopen("/Users/francis/Documents/out.txt","w",stdout);
	int T;
	cin>>T;
	for(int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		solve();
	}
}
