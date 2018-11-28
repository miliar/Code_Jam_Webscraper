#include <stdio.h>
void doe(int x)
{
	int k,c,s;
	scanf("%d %d %d",&k,&c,&s);
	printf("Case #%d: ",x);
	for(int i=1;i<=s;i++)
		printf("%d ",i);
	printf("\n");
}
int main()
{
	freopen("Din.in","r",stdin);
	freopen("Dout.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
		doe(i);
	return 0;
}
