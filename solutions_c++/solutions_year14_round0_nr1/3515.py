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

int arr[5][5],arr1[5][5];
int main()
{
    int test,ans1,ans2,i,k,j,anss,coutn;
    scanf("%d",&test);
    for(k=1;k<=test;k++)
    {
        coutn=0;
        scanf("%d",&ans1);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                scanf("%d",&arr[i][j]);
        }
        scanf("%d",&ans2);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                scanf("%d",&arr1[i][j]);
        }
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(arr[ans1][i]==arr1[ans2][j])
                {
                    if(coutn==0)
                    {
                        anss=arr[ans1][i];
                        coutn++;
                    }
                    else
                        coutn++;
                }
            }
        }
        if(coutn==0)
            printf("Case #%d: Volunteer cheated!\n",k);
        else if(coutn>1)
            printf("Case #%d: Bad magician!\n",k);
        else if(coutn==1)
            printf("Case #%d: %d\n",k,anss);
    }
    return 0;
}
