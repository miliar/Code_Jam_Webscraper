#include <cstdio>
#include <cstring>
int main()
{
	int T,n,m;
	scanf("%d\n",&T);
	char s[200];
	for(int tt=1;tt<=T;tt++)
	{
		printf("Case #%d: ",tt);
		gets(s);
		n=strlen(s);
		m=1;
		for(int i=1;i<n;i++)
			if(s[i]!=s[i-1]) ++m;
		if(s[n-1]=='+') --m;
		printf("%d\n",m);
	}
}

