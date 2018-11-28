#include <bits/stdc++.h>
#define ll long long int
#define MAX 1000000000000000000
using  namespace std;

ll power(int a, int b){
    ll val=1;
    for(int i=1;i<=b;i++){
        val*=a;
    }
    return val;
}

int main(){
    freopen("D-small-attempt1.in","r",stdin); freopen("00_output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++){
        int k,c,s;
        scanf("%d %d %d",&k, &c, &s);
        printf("Case #%d:",tc);
        for(ll i=1;i<=power(k,c);i=(i+power(k,c-1))){
            printf(" %lld",i);
        }
        printf("\n");
    }
}
