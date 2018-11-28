#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int test;
    int cases=0;
    for(scanf("%d",&test);test>0;--test){
        int n;
        int A[1010];
        int maxm=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&A[i]);
            maxm=max(maxm,A[i]);
        }
        int minm=maxm;
        for(int i=1;i<=maxm;i++){
            int tmp=i ;
            for(int j=0;j<n;j++){
                if(A[j]>i){
                    if(A[j]%i==0) tmp+=(A[j]/i-1);
                    else tmp+=(A[j]/i);
                }
            }
            minm=min(minm,tmp) ;
        }
        printf("Case #%d: %d\n", ++cases,minm) ;
    }
    return 0 ;
}
