#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,r,j;
    long long int i,n,n1,s,ans;
    scanf("%d",&t);
    for(j=1;j<=t;j++){
        int digits[10]={0},c=0;
        scanf("%lld",&n);
        if(n!=0){
            for(i=1;c!=10;i++){
            n1 = i*n;
            while(n1 > 0){
                r = n1%10;
                if(digits[r] == 0){
                    digits[r] = 1;
                    ++c;
                }
                n1 = n1/10;
            }
        }
            ans = (i-1)*n;
            printf("Case #%d: %lld\n",j,ans);
        }
        else{
            printf("Case #%d: INSOMNIA\n",j);
        }
    }
    return 0;
}
