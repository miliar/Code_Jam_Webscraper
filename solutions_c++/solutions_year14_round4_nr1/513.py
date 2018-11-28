#include<cstdio>
#include<queue>
#include<algorithm>
using namespace std;
priority_queue<int>q;
int n,x,a[100000];
int main()
{
	int T;
	scanf("%d",&T);
	for(int tcase=1;tcase<=T;tcase++)
	{
		scanf("%d%d",&n,&x);
		for(int i=1;i<=n;i++)scanf("%d",&a[i]);
		sort(a+1,a+n+1);
		int ans=0;
		while(!q.empty())q.pop();
		for(int i=n;i;i--)
		{
			if(q.empty()||q.top()<a[i])
			{
				ans++;
				q.push(x-a[i]);
			}
			else q.pop();
		}
		printf("Case #%d: %d\n",tcase,ans);
	}
}