#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <ctime>
#include <set>
#include <cassert>
using namespace std;
const int N=12345;
int cnt[N];
int main () {
    freopen("in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++) {
        int n;
        scanf("%d",&n);
        memset(cnt,0,sizeof cnt);
        for (int i=1;i<2*n;i++) {
            for (int j=1;j<=n;j++) {
                int k;
                scanf("%d",&k);
                cnt[k]++;
            }
        }
        printf("Case #%d:",cas);
        for (int i=1;i<=2500;i++) {
            if (cnt[i]&1) {
                printf(" %d",i);
            }
        }
        puts("");
    }
    return 0;
}
