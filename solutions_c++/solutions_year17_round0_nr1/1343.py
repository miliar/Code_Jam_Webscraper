#include<bits/stdc++.h>
#define MI 1000000000
#define X first
#define Y second
#define MP make_pair
#define MT make_tuple
#define EB emplace_back
using namespace std;
char s[1135];
int main()
{
	freopen("out.txt","w",stdout);
	//freopen("in.txt","r",stdin);
	int T,i,j,k,t,d,n,f=0,cot=0;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%s %d",s+1,&d);
		n=strlen(s+1);
		f=0;cot=0;
		for(i=1;i<=n-d+1;i++)
		{
			if(s[i]=='-')
			{
				cot++;
				for(j=i;j<i+d;j++)
					s[j]=s[j]=='+'?'-':'+';
			}
		}
		for(i=1;i<=n;i++)
		{
			if(s[i]=='-')
				f=1;
		}
		printf("Case #%d: ",t);
		if(f)printf("IMPOSSIBLE\n");
		else printf("%d\n",cot);

	}
}