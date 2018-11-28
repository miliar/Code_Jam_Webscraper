#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define rrep(i,x,y) for(i=x;i>=y;i--)
#define trv(y,x) for(typeof(x.begin())y=x.begin();y!=x.end();y++)
#define pb(f) push_back(f)
#define sc(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define pi(c) printf("%d\n",c)
#define pil(c) printf("%lld\n",c)
#define ll long long int
#define pii pair<int,int>
#define vi vector<int>
#define scs(a) scanf("%s",a)
using namespace std;
#define mod 1000000007
int main()
{
	int t,i,j,k;
	sc(t);
	
	int caase=1;
	while(t--)
	{
		int x,r,c;
		sc(x); sc(r); sc(c);
		if(x==1)
		{
			printf("Case #%d: GABRIEL\n",caase);
		}
		else if(x==2)
		{
			if((r*c)%2==0)
			{
				printf("Case #%d: GABRIEL\n",caase);
			}
			else
			printf("Case #%d: RICHARD\n",caase);
		}
		else if(x==3)
		{
			if((r*c)%3==0)
			{
				if(r+c==5||r+c==6||r+c==7)
				printf("Case #%d: GABRIEL\n",caase);
				else
				{
					printf("Case #%d: RICHARD\n",caase);
				}
			}
			else
			printf("Case #%d: RICHARD\n",caase);
		}
		else //(x==4)
		{
			if((r*c)%4==0)
			{
				if(r+c==7||r+c==8)
				{
					printf("Case #%d: GABRIEL\n",caase);
				}
				else 
				printf("Case #%d: RICHARD\n",caase);
			}
			else 
			printf("Case #%d: RICHARD\n",caase);
		}
		
		caase++;
	}
}
