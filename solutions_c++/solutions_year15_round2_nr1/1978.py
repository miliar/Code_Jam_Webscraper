#include <cstdio>
#include <cstring>

int n,m;
int f[1000009];
int l,cnt,T;
char s[19],t[19];

int main()
{
	scanf("%d",&T);
	for (int _=1;_<=T;++_)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;++i) f[i]=1000009;
		f[1]=1;
		for (int i=1;i<=n;++i)
		{
			if (f[i+1]>f[i]+1) f[i+1]=f[i]+1;
			sprintf(s,"%d",i);
			l=strlen(s);
			for (int j=0;j<l;++j) t[j]=s[l-1-j];
			t[l]='\n';
			sscanf(t,"%d",&m);
			if (f[m]>f[i]+1) f[m]=f[i]+1;
		}
		printf("Case #%d: %d\n",_,f[n]);
	}
	return 0;
}
