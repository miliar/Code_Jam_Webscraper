#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

pair<int,int> a[1005];
bool b[1005];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,t,n,i,j,k,x,s,s1,s2;
	for(scanf("%d",&T),t=1;t<=T;t++)
	{
		memset(b,0,sizeof(b));
		for(scanf("%d",&n),i=0;i<n;i++)
			scanf("%d",&x),a[i]=make_pair(x,i);
		sort(a,a+n);
		for(s=i=0;i<n;i++)
		{
			j=a[i].second;
			b[j]=1;
			for(s1=0,k=0;k<j;k++)
				s1+=!b[k];
			for(s2=0,k=j+1;k<n;k++)
				s2+=!b[k];
			s+=min(s1,s2);
		}
		printf("Case #%d: %d\n",t,s);
	}
	return 0;
}
