//  ...........
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
#define mod 1000000007
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
inline void fastwrite(int a){
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
}
*/

int main()
{
    int test,t,i,j,a,b,k;
    ll ans;
    scanf("%d",&test);
    for(t=1;t<=test;t++)
    {
        ans=0;
        scanf("%d %d %d",&a,&b,&k);
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                if((i&j)<k)
                    ans++;
            }
        }
        printf("Case #%d: %lld\n",t,ans);
    }
    return 0;
}
