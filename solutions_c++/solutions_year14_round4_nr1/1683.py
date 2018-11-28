#include <iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
//int ans1,ans2,left1,left2;
int ans;
//int tans1,tans2,tleft1,tleft2;
int a[100010],temp;
int visit[10010];
void solve(int ttt)
{
	ans=0;
	int n,x;
	cin >> n >> x;
	//ans1=1;ans2=0;left1=x;left2=x;
	for(int i=0;i<n;i++) scanf("%d",&a[i]);
	sort(a,a+n);
	for(int i=0;i<n;i++) visit[i]=0;
	for(int i=n-1;i>=0;i--)
	{
		if(visit[i]==1) continue;
			for(int j=i-1;j>=0;j--)
			{
				if(visit[j]==0 && a[i]+a[j]<=x)
				{
					//cout << "---" << i << " " << j << endl;
					visit[i]=1;visit[j]=1;
					ans++;
					break;
				}
			}
		if(visit[i]==0)
		{
			visit[i]=1;
			ans++;
		}
	}
	printf("Case #%d: %d\n",ttt+1,ans);
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	cin >> t;
	for(int i=0;i<t;i++) solve(i);
}