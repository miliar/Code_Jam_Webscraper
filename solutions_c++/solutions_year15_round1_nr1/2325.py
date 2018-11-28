#include<iostream>
#include<cstdio>
using namespace std;
int main() {
    // freopen("MM.txt","r",stdin);
    freopen("MMinput.txt","r",stdin);
    freopen("MMoutput.txt","w",stdout);
    int T,K,i;
    long long int N,ans,a,temp,sum,diff;
    scanf("%d",&T);
    for(K=1;K<=T;K++) {
        scanf("%lld",&N);
        long long int A[N];
        diff=0;
        ans=0;
        scanf("%lld",&A[0]);
        for(i=1;i<N;i++) {
            scanf("%lld",&A[i]);
            temp=A[i-1]-A[i];
            if(temp>diff) {
                diff=temp;
            }
            if(temp>0) {
                ans+=temp;
            }
        }
        sum=0;
        for(i=0;i<N-1;i++) {
            if(A[i]>=diff) {
                sum+=diff;
            } else {
                sum+=A[i];
            }
        }
        printf("Case #%d: %lld %lld\n",K,ans,sum);
    }
    return 0;
}
