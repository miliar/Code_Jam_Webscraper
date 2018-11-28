#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
double P[210];
int A[20];
int N,K;
int main(){
    freopen("bi.in","r",stdin);
    freopen("bo.out","w",stdout);
    int T;scanf("%d",&T);
    for(int tt=1;tt<=T;tt++){
        scanf("%d%d",&N,&K);
        for(int i=0;i<N;i++) scanf("%lf",&P[i]);
        double ans = 0.0;
        for(int n=0;n<(1<<N);n++) {
            int s = 0;
            for(int i=0;i<N;i++) {
                if(n&(1<<i)) {
                    A[s++] = i;
                }
            }
            if(s == K) {
                double sum = 0.0;
                for(int m=0;m<(1<<K);m++) {
                    int z = 0;
                    double p = 1.0;
                    for(int i=0;i<K;i++) {
                        if(m&(1<<i)) {
                            p *= P[A[i]];
                            z++;
                        }
                        else p *= (1.0 - P[A[i]]);
                    }
                    if(z*2 == K) {
                        sum += p;
                    }
                }
                if(ans < sum) ans = sum;
            }
        }
        printf("Case #%d: %.10f\n",tt,ans + 1e-9);
    }
    return 0;
}
