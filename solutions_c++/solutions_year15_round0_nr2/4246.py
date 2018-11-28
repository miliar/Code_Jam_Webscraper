#include <iostream>
#include <string.h>
#include <math.h>
#include <queue>
#include <algorithm>
#include <stdlib.h>
#include <map>
#include <set>
#include <stdio.h>
using namespace std;
#define LL long long
#define PI acos(-1.0)
const int mod=1e7+3;
const int INF=0x3f3f3f3f;
const double eqs=1e-9;
int a[2000];
int main()
{
        freopen("2.in","r",stdin);
        freopen("B.out","w",stdout);
        int t, i, j, n, ans, min1, Case=0;
        scanf("%d",&t);
        while(t--){
                scanf("%d",&n);
                for(i=0;i<n;i++){
                        scanf("%d",&a[i]);
                }
                min1=INF;
                for(i=1;i<=1000;i++){
                        ans=0;
                        for(j=0;j<n;j++){
                                ans+=(a[j]+(i-1))/i-1;
                        }
                        ans+=i;
                        min1=min(min1,ans);
                }
                printf("Case #%d: %d\n",++Case,min1);
        }
        return 0;
}
