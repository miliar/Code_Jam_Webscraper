#include <cstdio>
using namespace std;
int L,i,j,x,ans,T,re,ll;
bool v[17];
void work()
{
	ans=0;ll++;
	for (i=1;i<=16;i++) v[i]=0;
	scanf("%d\n",&L);
	for (i=1;i<=4;i++)
	for (j=1;j<=4;j++)
	{
		scanf("%d",&x);
		if (i==L) v[x]=1;
	}
	scanf("%d\n",&L);
	for (i=1;i<=4;i++)
	for (j=1;j<=4;j++)
	{
		scanf("%d",&x);
		if (i==L&&v[x]) ans++,re=x;
	}
	printf("Case #%d: ",ll);
	if (ans==0) {printf("Volunteer cheated!\n");return;};
	if (ans==1) {printf("%d\n",re);return;};
	if (ans>1) {printf("Bad magician!\n");return;};
	
}
int main()
{
	freopen ("a.in","r",stdin);
	freopen ("a.out","w",stdout);
	scanf("%d\n",&T);
	while (T) T--,work(); 
	return 0;
}

