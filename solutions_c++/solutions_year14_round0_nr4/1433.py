#include <cstdio>
#include <algorithm>
using namespace std;
double a[1002],b[1002];
int ans1,ans2,T,i,N,j,l;
bool v[1002];
void work()
{
	l++;
  	scanf("%d",&N);
  	for (i=1;i<=N;i++) scanf("%lf",&a[i]);sort(a+1,a+N+1);
  	for (i=1;i<=N;i++) scanf("%lf",&b[i]),v[i]=0;sort(b+1,b+N+1);
  	ans1=ans2=0;
  	for (i=1;i<=N;i++)
	{
  		for (j=1;j<=N;j++)
  			 if (!v[j]&&b[j]>a[i]) {v[j]=1;break;}
		if (j>N) for (j=1;j<=N;j++)
			 if (!v[j]) {ans1++;v[j]=1;break;}
	}
  	for (i=1;i<=N;i++) ans2+=(a[i]>b[ans2+1]);
  	printf("Case #%d: %d %d\n",l,ans2,ans1);
}
int main()
{
	freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
  	scanf("%d",&T);
  	while (T) T--,work();
  	return 0;
}
