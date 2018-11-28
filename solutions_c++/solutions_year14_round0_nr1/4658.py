#include<iostream>
#include<cstdio>
#include<climits>
#include<string>
#include<cstring>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<cmath>
#include<queue>
using namespace std;
#define inp(a) scanf("%d",&a)
#define line(a) printf("%d ",a);
#define next() printf("\n");
#define out(a) printf("%d\n",a)
#define swap(a,b) {a=a+b;a=a-b;b=a-b;}
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define ll long long int
#define mod 1000000007
#define getcx getchar_unlocked
/*inline void fscan(ll *a )
{
	ll n=0; int ch = getcx(); int sign = 1;
	while(ch < '0' || ch > '9')
	{
	if(ch == '-') sign=-1; ch = getcx();
	}
	while(ch >= '0' && ch <= '9')
	{
	n = (n << 3) + (n << 1) + ch - '0', ch = getcx();
	}
	*a = n * sign;
}*/
int i,j,k,t,mark1[100],n1,n2,f,l;
int main()
{
	inp(t);
	for(l=1;l<=t;l++)
	{
		inp(n1);
		for(i=1;i<=4;i++)
		{
			if(i!=n1)
			for(j=1;j<=4;j++) inp(k);
			else
			for(j=1;j<=4;j++)
			{
				inp(k);
				mark1[k]=1;
			}
		}
		inp(n2);
		ll c=0,orig=0;
		for(i=1;i<=4;i++)
		{
			if(i!=n2)
			{
				for(j=1;j<=4;j++) inp(k);
			}
			else
			for(j=1;j<=4;j++)
			{
				inp(k);
				for(f=1;f<=16;f++)
				{
					if(mark1[f]&&k==f)
					{
						orig=k;
						c++;break;
					}
				}	
			}
		}
		if(c==1)
		printf("Case #%d: %d\n",l,orig);
		else if(c>1)
		printf("Case #%d: Bad magician!\n",l);
		else
		printf("Case #%d: Volunteer cheated!\n",l);
		for(i=1;i<=16;i++) mark1[i]=0;
	}
	return 0;
}

