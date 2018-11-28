#include <stdio.h>
char s[1005],map[5005];
void doe()
{
	scanf("%s",s);
	int i,i2,start=2000,end=2000;
	map[start]=s[0];
	for(i=1;s[i]!=0;i++)
	{
		if(s[i]>=map[start])
			map[--start]=s[i];
		else
			map[++end]=s[i];
	}
	for(i=start;i<=end;i++)
		printf("%c",map[i]);
	printf("\n");
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int n,i;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
		printf("Case #%d: ",i),doe();
	return 0;
}
