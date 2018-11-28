#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("large.txt","w",stdout);
    int T,x,y;
    cin>>T;

    for(int i=1;i<=T;++i){
        double C=0,F=0,X,cost=0,ca=0,cb=0,op=0;
        cin>>C>>F>>X;
        op=2;
        while(true){
            ca=X/op;
            cb=C/op+X/(op+F);
            if(ca>cb){

                cost+=C/op;
                op+=F;
            }else {
                cost+=ca;
                break;
            }
        }
        printf("Case #%d: %.7lf\n",i,cost);

    }
    return 0;
}
