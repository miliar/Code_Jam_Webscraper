#include <bits/stdc++.h>
using namespace std;

//long long mod = 1000000007;
//
//long long mypow(long long a,int b){
//    if(b==0)return 1;
//    long long tmp = mypow(a,b/2);
//    tmp = (tmp*tmp)%mod;
//    return (b&1)? ((tmp*a)%mod):tmp;
//}

int main() {
    int T;
    double C,F,X,ans;
    scanf("%d",&T);
    for(int t=1;t<=T;t++){
        scanf("%lf %lf %lf",&C,&F,&X);
        ans = 0;
        int it = (X/C) -(2/F) - 1;
        int i=0;
        while(i<=it){
            ans += C/(2+(i*F));
            i++;
        }
        ans += X/(2+(i*F));
        ans = min(ans,X/2);
        ans = min(ans,(C/2)+(X/(2+F)));
        printf("Case #%d: %0.7lf\n",t,ans);

    }
    return 0;
}
