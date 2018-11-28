/* shakti11094 : Shakti Kheria */
#include<bits/stdc++.h>

#define ll long long
#define MP(a,b) make_pair(a,b)
#define PB(a) push_back(a)
#define fi first
#define se second
#define s(a) scanf("%d",&a);
#define sl(a) scanf("%lld",&a);
#define s64(a) scanf("%I64d",&a);
#define sf(a) scanf("%f",&a);
#define sd(a) scanf("%lf",&a);
#define sld(a) scanf("%llf",&a);
#define ss(a) scanf("%s",a);
#define fillin(a,b) memset(a,b,sizeof(a))
using namespace std;

int main(){
    ll t,x,r,c,tc=0;
    sl(t);
    while(t--){
        printf("Case #%lld: ",++tc);
        sl(x);sl(r);sl(c);
        if(x==1)
            printf("GABRIEL\n");
        else if(x==2){
            if((r*c)%2)
                printf("RICHARD\n");
            else
                printf("GABRIEL\n");
        }
        else if(x==3){
            if(((r*c)%3) || ((r*c)==3))
                printf("RICHARD\n");
            else
                printf("GABRIEL\n");
        }
        else if(x==4){
            if(((r*c)%4) || ((r*c)<=8))
                printf("RICHARD\n");
            else
                printf("GABRIEL\n");
        }
    }
    return 0;
}
