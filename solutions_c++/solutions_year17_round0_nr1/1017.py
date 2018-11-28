#include <bits/stdc++.h>
using namespace std;

#define sd(x) scanf("%d",&x)
#define su(x) scanf("%u",&x)
#define slld(x) scanf("%lld",&x)
#define sc(x) scanf("%c",&x)
#define ss(x) scanf("%s",x)
#define sf(x) scanf("%f",&x)
#define slf(x) scanf("%lf",&x)
#define ll long long int
#define mod(x,n) (x+n)%n

char S[1007];
char Srev[1007];

int answer(char S[],int k,int n)
{
	int i,j,m=0;	

	for(i=0;i<n;i++)
	{
		if(S[i]=='-')
		{
			for(j=i;j<i+k;j++)
			{
				if(j>=n)
					return -1;
				if(S[j]=='+')
					S[j]='-';
				else
					S[j]='+';
			}
			m++;
		}
	}	
	return m;
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int i,j,k,l,m,n,t,tno,ans1,ans2;

	sd(t);	tno=1;
	while(tno<=t)
	{

		ss(S);	sd(k);	n = strlen(S);

		for(i=0;i<n;i++)
			Srev[n-1-i] = S[i];
		Srev[n] = '\0';

		ans1 = answer(S,k,n);
		ans2 = answer(Srev,k,n);

		if(ans1==-1 && ans2==-1)
			printf("Case #%d: IMPOSSIBLE\n",tno);
		else if(ans1==-1)
			printf("Case #%d: %d\n",tno,ans2);
		else if(ans2==-1)
			printf("Case #%d: %d\n",tno,ans1);
		else
			printf("Case #%d: %d\n",tno,min(ans1,ans2));

		tno++;
	}	
	
	return 0;
}