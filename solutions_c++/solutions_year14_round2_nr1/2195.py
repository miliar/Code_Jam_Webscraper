#include<stdio.h>
#include<string.h>
int sta[2][111];
void deal(char*s,char*p,int k)
{
	int len = strlen(s),i,j = -1;
	for(i = 0;i < len;)
	{
		p[++j] = s[i];
		while(i < len && s[i] == p[j])++i,++sta[k][j];	
	}
	p[++j] = '\0';
}
int ABS(int x)
{
	return x > 0 ? x : -x ;
}
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int t,n,cse,i,l,ans;
	char s1[111],s2[111],a[111],b[111];
	scanf("%d",&t);
	for(cse=1;cse<=t;++cse)
	{
		scanf("%d",&n);//n == 2
		scanf("%s",s1);
		scanf("%s",s2);
		if(strcmp(s1,s2) == 0)
		{
			printf("Case #%d: %d\n",cse,0);
			continue;
		}
		memset(sta,0,sizeof sta);
		deal(s1,a,0);
		deal(s2,b,1);
		if(strcmp(a,b) != 0)
		{
			printf("Case #%d: Fegla Won\n",cse);
			continue;
		}
		l = strlen(a);
		ans = 0;
		for(i = 0;i < l;++ i)ans += ABS(sta[0][i] - sta[1][i]);
		printf("Case #%d: %d\n",cse,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
