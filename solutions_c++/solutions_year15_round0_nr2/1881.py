#include <iostream>
#include <string>
#include <string.h>
#include <cstdio>
#include <queue>

using namespace std;
const int maxn = 1005;

int n;
int p[maxn];
priority_queue<int> que;

int main(){

    int t; scanf("%d",&t);
    for(int it=1;it<=t;it++){
        scanf("%d",&n);
        for(int i=1;i<=n;i++) scanf("%d",&p[i]);

        int ans = maxn;
        for(int i=1;i<=maxn;i++){
            if ( i>ans ) break;

            int sum = 0;
            for(int j=1;j<=n;j++){
                int k = max(0,p[j]-i);
                if ( k>0 ){
                    if ( k%i==0 ) k = k/i;
                    else k = k/i+1;
                }
                sum += k;
            }
            ans = min( ans , sum+i );
        }
        printf("Case #%d: %d\n",it,ans);
    }

    return 0;
}