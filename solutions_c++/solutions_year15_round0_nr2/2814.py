#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cassert>
#define ll long long
using namespace std;

int n;
int num[1010];
int pos[1010];
int tn[1010];
vector<int> V;
int Min(int a,int b)
{
    return a>b?b:a;
}
int Max(int a,int b)
{
    return a>b?a:b;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.out","w",stdout);
    int T;
    int Case=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%d",&n);
        int maxn=0;
        int i=0,j;
        memset(pos,0,sizeof pos);
        while(i<n)
        {
            scanf("%d",&num[i]);
            i++;
        }
        i=0;
        while(i<n)
        {
            maxn=Max(maxn,num[i]);
            pos[num[i]]++;
            i++;
        }
        int ans=maxn;
        i=2;
        while(i<maxn)
        {
            j=i+1;
            tn[i]=0;
            while(j<=maxn)
            {
                int temp=(j-1)/i;
                tn[i]+=temp*pos[j];
                j++;
            }
            ans=Min(ans,tn[i]+i);
            i++;
        }
        printf("Case #%d: %d\n",Case++,ans);
    }

    return 0;
}
