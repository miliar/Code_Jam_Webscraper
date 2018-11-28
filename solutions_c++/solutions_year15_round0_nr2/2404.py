#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<string>
#include<string.h>
#include<vector>
#include<map>
using namespace std;

#define mx 10000000
#define ip freopen("in.txt","r",stdin)

#define sint1(a) scanf("%d",&a)
#define sint2(a,b) scanf("%d %d",&a,&b)
#define sint3(a,b,c) scanf("%d %d %d",&a,&b,&c)


#define sch1(a) scanf("%c",&a)
#define sch2(a,b) scanf("%c %c",&a,&b)
#define sch3(a,b,c) scanf("%c %c %c",&a,&b,&c)


#define sll1(a) scanf("%lld",&a)
#define sll2(a,b) scanf("%lld %lld",&a,&b)
#define sll3(a,b,c) scanf("%lld %lld %lld",&a,&b,&c)

#define ll long long int

#define lpi0(a,b) for(int a=0;a<b;a++)
#define lpd0(a,b) for(int a=b-1;a>=0;a--)

#define lpi1(a,b) for(int a=1;a<=b;a++)
#define lpd1(a,b) for(int a=b;a>0;a--)

#define vi vector<int>
#define pii pair<int,int>
#define mp make_pair

#define mm(a,b) memset(a,b,sizeof(a))
int f[1010];
int a[1010];


int main()
{
//    ip;
//    freopen("out.txt","w",stdout);

    int t;
    sint1(t);
    int cs=1;

    while(t--)
    {
    	int d;
    	sint1(d);
    	int j=0;
    	mm(a,0);
    	mm(f,0);

    	for(int i=0;i<d;i++)
    	{
    		int x;
    		sint1(x);
    		f[x]++;
    		if(f[x]==1)
    		{
    			a[j++]=x;
    		}
    	}

		sort(a,a+j);
		int p=a[j-1];
		int ans=p;
		for(int i=2;i<=p;i++)
		{
			int anss=0;
			for(int k=j-1;k>=0;k--)
			{
				if(i>=a[k])
				{
					break;
				}

				int x=a[k];
				int y=f[x];

				int g=x/i;

				if(g*i==x)
				{
					g--;
				}

				anss=anss+y*g;
			}
			ans=min(ans,anss+i);
		}


		printf("Case #%d: %d\n",cs++,ans);

    }




}



