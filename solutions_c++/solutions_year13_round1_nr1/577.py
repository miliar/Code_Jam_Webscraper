#include<stdio.h>
#include<stdlib.h>
#include<iostream>
using namespace std;
// pi( (r+1^2 - (r)^2 ) )
// pi ( r^2 +2r +1 -r^2 )
//  2r+1
// r r+2 r+4 . . . . . . r+2n
// 2r+1 2r+5 2r+9 . . . . 2r+4n+1
// assume we draw t circle
// S = a1 + a2 + . . . + an
// S = a1 + a1+r+a1+2r+...+a1+(n-1)r
// S = na1 + 2(n-1)(n)
// S = n(2r+1 + 2(n-1))
// binarysearch on N
// (n+1)r + (n)(n+1) = (n+1) (r+n)

void solve(){
    long long r,t;
    cin >> r >> t;
    long long s=1,e=2e18;
    long long ret=0;
    while(s<=e){
        long long m=(s+e)/2;
        if((r+m) <=(t/(m) +1 ) /2 ){
            ret=m;
            s=m+1;
        }
        else e=m-1;
    }
    printf("%lld\n",ret);
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
