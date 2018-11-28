#include<cstdio>
#include<queue>
#include<cstring>

int t;
char input[2010];
int k;
int p,A;
bool possible;
int x,y;
int flip[2010];

int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);

	scanf("%d\n",&t);
	for(int n=1;n<=t;n++)
	{
		p=A=0;
		x=y=0;
		possible=true;
		memset(input,0,2000);
		memset(flip,-1,2000);

		scanf("%s %d\n",input,&k);

		for(;input[p+k-1]=='-'||input[p+k-1]=='+';p++)
		{
			if(flip[x]==p) x++;
			if(((y-x)%2==0&&input[p]=='-')||((y-x)%2==1&&input[p]=='+'))
			{
				flip[y++]=p+k;
				A++;
			}
		}
		for(;(input[p]=='-'||input[p]=='+')&&possible;p++)
		{
			if(flip[x]==p) x++;
			if(((y-x)%2==0&&input[p]=='-')||((y-x)%2==1&&input[p]=='+')) possible=false;
		}

		printf("Case #%d: ",n);
		if(!possible) printf("IMPOSSIBLE\n");
		else printf("%d\n",A);
	}
	return 0;
}
