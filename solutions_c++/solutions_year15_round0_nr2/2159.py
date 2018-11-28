#include<bits/stdc++.h>
using namespace std;

int n,a[1005];

inline int cal(int x)
{
	int i,s;
	for(s=i=0;i<n;i++)
		s+=a[i]/x;
	return s+x;
}

int main()
{freopen("E:/in.txt","r",stdin);freopen("out.txt","w",stdout);
	int T,t,i,s;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		scanf("%d",&n);
		for(s=1<<30,i=0;i<n;i++)
			scanf("%d",a+i),--a[i];
		for(i=1;i<=1000;i++)
			s=min(s,cal(i));
		printf("Case #%d: %d\n",t,s);
	}
	return 0;
}
