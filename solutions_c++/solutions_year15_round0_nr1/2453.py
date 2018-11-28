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
int main()
{
//    ip;
//    freopen("out.txt","w",stdout);

    int t;
    sint1(t);
    int cs=1;

    while(t--)
    {
    	int n;
    	char s[1010];

    	sint1(n);
    	getchar();
    	cin>>s;

    	int ans=0;
    	int c=0;
    	for(int i=0;i<=n;i++)
    	{
    		int x=s[i]-48;
    		if(c<i)
    		{
    			ans=ans+i-c;
    			c=i;
    		}

    		c=c+x;
    	}

    	printf("Case #%d: %d\n",cs++,ans);
    }


}
