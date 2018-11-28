//  google_codejam_2014_Deceitful_War.cpp ...........
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <complex>
#include <climits>
#define MAX 20005
#define MAXX 25
#define MA 1100000
#define mod 1000000009
typedef long long ll;
typedef unsigned long long ull;
using namespace std;


/*int read()
{
    register int ch = getchar_unlocked();
    int a = 0;
    for(;(ch<48 || ch>57);ch = getchar_unlocked());
    for(;ch>47 && ch<58;ch = getchar_unlocked())
    {
        a = (a<<1) + (a<<3) + ch - 48;
    }
    return a;
}*/
/*char read1()
{
    register char a;
    asd: a=getchar_unlocked();
    if(a>='A' && a<='Z')
    {
        return a;
    }
    else
        goto asd;
}*/
/*
inline void fastwrite(ll a){
register char c;
char snum[20];
int i=0;
do{
snum[i++]=a%10+48;
a=a/10;
}while(a!=0);
i=i-1;
while(i>=0)
putchar_unlocked(snum[i--]);
putchar_unlocked('\n');
}*/

double n[1005],k[1005],visit[1005];
int main()
{
    int test,kk,coutn,dwar,net,war,i,j,total,ind;
    scanf("%d",&test);
    for(kk=1;kk<=test;kk++)
    {
        dwar=coutn=ind=war=net=0;
        memset(visit,0,sizeof(visit));
        scanf("%d",&total);
        for(i=0;i<total;i++)
            scanf("%lf",&n[i]);
        for(i=0;i<total;i++)
            scanf("%lf",&k[i]);
        sort(n,n+total);
        sort(k,k+total);
        for(i=0;i<total;i++)
        {
            for(j=0;j<total;j++)
            {
                if(n[i]>k[j] && visit[j]==0)
                {
                    visit[j]=1;
                    dwar++;
                    break;
                }
            }
        }
        memset(visit,0,sizeof(visit));
        for(i=total-1;i>=0;i--)
        {
            coutn=0;
            for(j=0;j<total;j++)
            {
                if(n[i]>k[j])
                {
                    if(visit[j]==0)
                        coutn++;
                }
                else
                    break;
            }
            if(coutn==(total-net))
            {
                visit[ind]=1;
                war++;
                ind++;
            }
            else
            {
               visit[j]=1;
            }
            net++;
        }
        printf("Case #%d: %d %d\n",kk,dwar,war);
    }
    return 0;
}
