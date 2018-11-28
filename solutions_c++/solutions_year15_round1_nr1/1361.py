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

int valid(int *ar,int N,int r)
{
    int i;
    for(i=1;i<N;i++)
    {
        if(ar[i-1]-ar[i]>r)
            return 0;
    }
    return 1;
}
int getrate(int *ar,int N)
{
    int mid,low=0,high=10005;
    while(low+1<high)
    {
        mid=(low+high)/2;
        if(valid(ar,N,mid))
            high=mid;
        else
            low=mid;
    }
    if(valid(ar,N,low))
        return low;
    return low+1;
}

int fixedrate(int *ar,int N)
{
int tp=getrate(ar,N);
int i,rt=0;
for(i=0;i<N-1;i++)
    rt+=min(tp,ar[i]);
return rt;
}

int main()
{   freopen("A-large.in", "r", stdin);
    freopen("result1.txt", "w", stdout);
    int i,j,N,T;
    scanf("%d",&T);
    for(i=1;i<T+1;i++)
    {
    scanf("%d",&N);
    int ar[N+1];
    for(j=0;j<N;j++)
        scanf("%d",&ar[j]);
    int ans1=0,ans2=0;
    for(j=1;j<N;j++)
    {
    ans1+=max(0,ar[j-1]-ar[j]);
    }
    ans2=fixedrate(ar,N);
    printf("Case #%d: %d %d\n",i,ans1,ans2);
    }
}
