#include <iostream>
#include <cstdio>
using namespace std;

double c,f,x,t,tmp,a,kt,wt;
int n;
bool b;
void cek(){
    while(b){
        tmp=(x/kt);
        a=(c/kt)+(x/(kt+f));
        if(tmp<=a){
            b=false;
            t=wt+tmp;
        }
        else{
            wt+=(c/kt);
        }
        kt+=f;
    }
}

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("out.out","w",stdout);
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        scanf("%lf %lf %lf",&c,&f,&x);
        b=true;kt=2;wt=0;
        cek();
        printf("Case #%d: %.7lf\n",i,t);
    }
    return 0;
}
