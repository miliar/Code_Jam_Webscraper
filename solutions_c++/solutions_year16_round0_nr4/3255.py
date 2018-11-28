#include <bits/stdc++.h>
using namespace std;

int main(){
    int K,C,S,t;
    freopen("D-small-attempt2.in","r",stdin);
    freopen("D-small-attempt2.out","w",stdout);
    cin>>t;
    for(int ca=1;ca<=t;ca++){
        cin>>K>>C>>S;
        printf("Case #%d:",ca);
        for(int i=1;i<=K;i++){
            printf(" %d",i);
        }
        printf("\n");
    }
    return 0;
}
