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
#define op freopen("out.txt","w",stdout)

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

int p[20];

bool check()
{
    for(int i=0;i<=9;i++)
    {
        if(p[i]==0)
            return false;
    }

    return true;
}
int main()
{
//    ip;
//    op;

    int t;

    sint1(t);

    int cs=1;
    while(t--)
    {
        int x;
        sint1(x);
        mm(p,0);
        if(x==0)
        {
            printf("Case #%d: INSOMNIA\n",cs++);
            continue;
        }

        int y=0;
        while(check()!=true)
        {
            y=y+x;

            int z=y;
            while(z)
            {
                int a=z%10;
                p[a]=1;
                z=z/10;
            }
        }

        printf("Case #%d: %d\n",cs++,y);


    }

}
