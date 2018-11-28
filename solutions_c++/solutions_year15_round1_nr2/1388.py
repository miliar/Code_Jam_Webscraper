#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

long long gcd(long long a,long long b)
{
    if(b==0)
        return a;
    return gcd(b,a%b);
}

long long lcm(long long a,long long b)
{
    long long g=gcd(a,b);
    return (a*b)/g;
}

int assigned(int *ar,int B,int N)
{
    int i,j,rt=0;
    long long ptime[B+1];
    for(i=0;i<B;i++)
        ptime[i]=0;
    int mx,id;
    for(i=1;i<N+1;i++)
    {
        mx=ptime[0];id=0;
        for(j=0;j<B;j++)
        {
            if(mx>ptime[j])
            {
                mx=ptime[j];
                id=j;
            }
        }
       // printf("%d\n",id+1);
        ptime[id]+=ar[id];
    }
    return id+1;
}
int main()
{   freopen("B-small-attempt0.in", "r", stdin);
    freopen("result1.txt", "w", stdout);
    int i,j,N,B,T;
    scanf("%d",&T);
    for(i=1;i<T+1;i++)
    {
    scanf("%d %d",&B,&N);
    int ar[B+1];
    for(j=0;j<B;j++)
        scanf("%d",&ar[j]);
    int ans1=0;
    long long tp,lm=ar[0];
    for(j=1;j<B;j++)
        lm=lcm(lm,ar[j]);
    tp=0;
    for(j=0;j<B;j++)
        tp+=lm/ar[j];
    if(N%tp==0)
    ans1=assigned(ar,B,tp);
    else
    ans1=assigned(ar,B,N%tp);
    printf("Case #%d: %d\n",i,ans1);
    }
}
