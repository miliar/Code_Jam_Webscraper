#include<iostream>
#include<cstdio>
using namespace std;
int main() {
    // freopen("StandingOvation.txt","r",stdin);
    freopen("SOinput.txt","r",stdin);
    freopen("SOoutput.txt","w",stdout);
    int T,K,max,ans,total,i;
    scanf("%d",&T);
    for(K=1;K<=T;K++) {
        scanf("%d",&max);
        char S[max+3];
        scanf("%s",S);
        total=(S[0]-48);
        ans=0;
        for(i=1;i<=max;i++) {
            if(S[i]==48) {
                continue;
            }
            if(total>=i) {
                total+=(S[i]-48);
                continue;
            }
            ans+=(i-total);
            total+=(i-total+S[i]-48);
        }
        printf("Case #%d: %d\n",K,ans);
    }
}
