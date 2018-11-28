#include<cstdio>
#include<cstring>
#include<string>
#include<cmath>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int t, n, a[1005], i, j, s[1005];
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(int cnt = 1;cnt <= t;cnt++){
        scanf("%d",&n);
        for(i=0;i<n;i++){
            scanf("%d",a+i);
        }
        int ret = 0;
        for(i=0;i<n;i++)s[i] = a[i];
        while(n){
            int mi = 1000000001, idx;
            for(i=0;i<n;i++){
                if(s[i]<mi){
                    mi = s[i];
                    idx = i;
                }
            }
            ret += min(idx, n - 1 - idx);
            for(i=idx;i<n-1;i++)s[i] = s[i+1];
            n--;
        }

        printf("Case #%d: %d\n",cnt,ret);
    }
    return 0;
}
