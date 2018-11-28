#include <stdio.h>
char s[105];
void doe(int x)
{
	int n=0,i,i2,check,ans=0;
	scanf("%s",s);
	printf("Case #%d: ",x);
	for(n=0;s[n]!=0;n++);
	for(i=1;i<n;i++)
		if(s[i]!=s[i-1])
			ans++;
	if(s[n-1]=='-')
		ans++;
	printf("%d\n",ans);
}
int main()
{
	freopen("Bin.in","r",stdin);
	freopen("Bout.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
		doe(i);
	return 0;
}
