//  google_codejam_2014_Cookie_Clicker_Alpha.cpp...........
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

int main()
{
    int test,k,i;
    double c,f,x,temp,temp1,ans,rate;
    scanf("%d",&test);
    for(k=1;k<=test;k++)
    {
        rate=2.0000000;
        temp=ans=temp1=0.0000000;
        scanf("%lf %lf %lf",&c,&f,&x);
        ans=(x/rate);
        temp=(c/rate);
        rate+=f;
        temp1=(x/rate);
        temp+=temp1;
        while(temp<ans)
        {
            i++;
            ans=temp;
            temp-=temp1;
            temp+=(c/rate);
            rate+=f;
            temp1=(x/rate);
            temp+=temp1;
        }
        printf("Case #%d: %.7lf\n",k,ans);
    }
    return 0;
}
