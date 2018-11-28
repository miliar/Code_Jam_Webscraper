#include <bits/stdc++.h>
using namespace std;
int mask;
void update(int n){
    while(n){
        int d = n%10;
        n/=10;

        mask |= (1<<d);

    }
    return ;
}
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,N;
    scanf("%d",&T);
    for(int tc=1;tc<=T;tc++){
        scanf("%d",&N);
        int n=N;
        if(n==0){
            printf("Case #%d: INSOMNIA\n",tc);
            continue;
        }
        mask=0;
        update(n);
        while(mask!=(1<<10)-1){
              n += N;
              update(n);
        }
        printf("Case #%d: %d\n",tc,n);
    }
}
