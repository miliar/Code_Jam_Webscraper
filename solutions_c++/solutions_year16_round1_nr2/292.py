#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
#include <math.h>
#include <algorithm>
using namespace std;
typedef long long ll;

int cnt[2505];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("blarge.txt","w",stdout);
    int T,Case=1;
    for(scanf("%d",&T);Case<=T;Case++){
        memset(cnt,0,sizeof(cnt));
        int n,t;
        scanf("%d",&n);
        for(int i=0;i<2*n-1;i++){
            for(int j=0;j<n;j++){
                scanf("%d",&t);
                cnt[t]++;
            }
        }
        printf("Case #%d:",Case);
        for(int i=1;i<=2500;i++){
            if(cnt[i]&1)printf(" %d",i);
        }
        puts("");
    }
    return 0;
}

