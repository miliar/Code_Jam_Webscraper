#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<stdio.h>
#include<set>
#include<cmath>

using namespace std;
int a[1004];
int main() {
    freopen("exam.in","r",stdin);
    freopen("exam.out","w",stdout);
    int T,D;

    scanf("%d",&T);
    for(int t=1; t<=T; t++)
    {
        int ans=0;
        scanf("%d",&D);
        for(int i=0; i<D; i++)
        {
            scanf("%d",&a[i]);
            ans=max(ans,a[i]);
        }

        sort(a,a+D);

        int p=2;
        while(p<ans)
        {
            int sum=p;
            for(int i=0; i<D; i++)
                sum+=(a[i]-1)/p;
            ans = min(ans, sum);
            p++;
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
