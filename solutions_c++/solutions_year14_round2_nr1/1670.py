#include <cstring>
#include <cstdlib>
#include <cstdio>

int T,n,m,cnt,ans,c[109][109],f[109][109],d[109];
char str[109],t,s[109][109];

int main()
{
	freopen("input","r",stdin);
	freopen("output","w",stdout);
	scanf("%d",&T);
	for (int _=1;_<=T;++_)
	{
		printf("Case #%d: ",_);
		scanf("%d%*c",&n);
		for (int i=0;i<n;++i)
		{
			gets(str);
			m=0;
			s[i][m]=t=*str;
			c[i][m]=0;
			for (char *p=str;*p;++p)
			{
				if (*p==t) ++c[i][m];
				else
				{
					++m;
					s[i][m]=t=*p;
					c[i][m]=1;
				}
			}
			s[i][++m]='\0';
		} 
		for (int i=1;i<n;++i) if (strcmp(s[i-1],s[i])) goto NO;
		memset(f,0,sizeof(f));
		for (int i=0;i<n;++i) for (int j=0;j<m;++j) ++f[j][c[i][j]];
		for (int j=0;j<m;++j)
		{
			cnt=0;
			for (int i=0;i<=100;++i) if ((cnt+=f[j][i])>n/2)
			{
				d[j]=i;
				break;
			}
		}
		ans=0;
		for (int i=0;i<n;++i) for (int j=0;j<m;++j) ans+=abs(c[i][j]-d[j]);
		printf("%d\n",ans);
		continue;
		NO:puts("Fegla Won");
	}
}