#include<bits/stdc++.h>
using namespace std;
int n,a[1005];
void execute()
{
	int ans=1000;
	scanf("%d",&n);
	for(int i=1; i<=n; i++) scanf("%d",&a[i]);
	for(int i=1; i<=1000; i++)
	{
		int res = i;
		for(int j=1; j<=n; j++) res+=(a[j]-1)/i;
		ans = min(ans,res);
	}
	cout<<ans<<endl;
}
int main()
{
	freopen("B.inp","r",stdin);
	freopen("B.out","w",stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++)
	{
		printf("Case #%d: ",tc);
		execute();
	}
	return 0;
}
