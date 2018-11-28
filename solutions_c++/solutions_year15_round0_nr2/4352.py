#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;


const int maxn = 1000+20;
int p[maxn];

int main() {
    int T;
    scanf("%d",&T);
    int D;
    int in = 1;
    while(T--) {
        scanf("%d",&D);
        for(int i=1; i<=D; i++)
            scanf("%d",&p[i]);
        sort(p+1,p+1+D);
        int ans = p[D];
        int maxa = ans;
        for(int i=1; i<=maxa; i++) {
            for(int j=i;j>=(int)ceil(i*1.0/D);j--) {
                int keqieshu = i-j;
                int maxtmp = (int)ceil(p[D]*1.0/(j+1));
                for(int k=D-1;k>=1;k--) {
                    if(keqieshu == 0) {
                        maxtmp = max(maxtmp,p[k]);
                        break;
                    }
                    if(keqieshu >= j) {
                        keqieshu -= j;
                        maxtmp = max(maxtmp,(int)ceil(p[k]*1.0/(j+1)));
                    }
                    else {
                        maxtmp = max(maxtmp,(int)ceil(p[k]*1.0/(keqieshu+1)));
                        keqieshu = 0;
                    }
                }
                ans = min(ans,maxtmp + i);
            }
        }
        printf("Case #%d: %d\n",in++,ans);
    }

}

