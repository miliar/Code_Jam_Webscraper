#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <cmath>
#include <vector>
#include <string>
#include<iomanip>
#define Mod (1000000007LL)
#define eps (1e-12)
#define Pi (acos(-1.0))
using namespace std;
int n,X;
int S[11000];
int ans;
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("A-large (1).out","w",stdout);
    int T;
    scanf("%d",&T);
    int cas=0;
    while(T--)
    {
        scanf("%d%d",&n,&X);
        for(int i=0;i<n;i++)
        scanf("%d",&S[i]);
        ans=n;
        int j=n-1;
        sort(S,S+n);
        for(int i=0;i<j;i++)
        {
            if(j<=i) break;
            while(S[i]+S[j]>X&&j>i) j--;
            if(j<=i) break;
            ans--;j--;
            //printf("j:%d\n",j);
        }
        printf("Case #%d: %d\n",++cas,ans);
    }
    return 0;
}
