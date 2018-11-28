#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long n,ans;
    int t;
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    int p=1;
    while(t--){
        int a[13]={0};
        int c=0;
        scanf("%lld",&n);
        if(n==0){
            printf("Case #%d: INSOMNIA\n",p);
        }
        else{
            for(long long i=1;;i++){
                long long k = i*n;
                ans = k;
                while(k){
                    int r = k%10;
                    if(a[r]==0){
                        a[r] = 1;
                        c++;
                    }
                    k /= 10;
                }
                if(c==10){
                    break;
                }
            }
            printf("Case #%d: %lld\n",p,ans);
        }
        p++;
    }
}
