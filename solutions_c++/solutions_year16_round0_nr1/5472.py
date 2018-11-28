#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main(){
    freopen("A-large.in","r",stdin); freopen("00_output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        bool found=false;
        int n,counter=0;
        scanf("%d",&n);
        int marker[10];
        memset(marker,0,sizeof(marker));
        if (n==0){
            printf("Case #%d: INSOMNIA\n",i);
            continue;
        }
        for(ll j=1;j<10000000 && !found;j++){
            ll val=j*n;
            ll saveVal=val;
            int digits=log10(val);
            for(;val>0;){
                if (marker[val%10]==0){
                    marker[val%10]=1;
                    counter++;
                }
                val/=10;
            }
            if (counter>=10){
                found=true;
                printf("Case #%d: %lld\n",i,saveVal);
            }
        }

        if (!found)
            printf("Case #%d: INSOMNIA\n",i);

    }
}
