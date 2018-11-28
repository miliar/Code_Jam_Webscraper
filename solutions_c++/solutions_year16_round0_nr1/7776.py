#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int s[105];
void check(int x)
{
	while (x)
	{
		s[x%10]=1;
		x/=10;
	}
}
int main()
{
	int n,judge,flag,i,j,T,t;
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%d",&n);
		printf("Case #%d: ",t);
		if (n==0){printf("INSOMNIA\n"); continue; }
		judge=0;
		memset(s,0,sizeof(s));
		for (i=1;;i++)
		{
			flag=1;
			check(n*i);
			for (j=0;j<10;j++)
				if (s[j]==0) flag=0;
			if (flag) {judge=1; break;}
		//	printf("%d %d\n",n,n*i);
		}
		printf("%d\n",n*i);
	}
	return 0;
} 
