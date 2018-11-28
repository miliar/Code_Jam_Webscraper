#include <iostream>
#include <string.h>
#include <cstdio>
#include <stack>
using namespace std;
#define M 105
#define LL long long 
#define BB
int c,n,m,t;
char s[105];
int p[105];
void re(int x)
{
	for (int i=1;i<=(x+1)/2;i++)
	{
		p[i]^=1;
		if (x+1-i!=i)
			p[x+1-i]^=1;
		swap(p[i],p[x+1-i]);
	}
}
int main()
{
#ifdef BB	
	freopen("E:\\B-large.in","r",stdin);
	freopen("E:\\B-large.out","w",stdout);
#endif
	int cc=1;
	cin>>t;
	while (t--)
	{
		cin>>s;
		int l=strlen(s),ans=0;
		for (int i=0;i<l;i++)
		{
			if (s[i]=='-')
				p[i+1]=0;
			else if (s[i]=='+')
				p[i+1]=1;
		}
		int i=l;
		while (i>0)
		{
			if (p[i]==0&&p[1]==0)
			{
				re(i);
				ans++;
			}
			else if (p[i]==0&&p[1]==1)
			{
				int tt=0;
				while (p[tt+1]==1)
					tt++;
				re(tt);
				ans++;
			}
			else if (p[i]==1)
				i--;
		}
		cout<<"Case #"<<cc++<<": "<<ans<<endl;
	}
#ifdef BB
	fclose(stdin);
	fclose(stdout);
#endif
	return 0;
}
