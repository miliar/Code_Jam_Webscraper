#include<iostream>
#include<cstdio>
using namespace std;
int main() {
    // freopen("OO.txt","r",stdin);
    freopen("OOinput.txt","r",stdin);
    freopen("OOoutput.txt","w",stdout);
    int T,X,R,C,K,flag;
    scanf("%d",&T);
    for(K=1;K<=T;K++) {
        scanf("%d%d%d",&X,&R,&C);
        flag=1;
        if((R*C)%X!=0) {
            flag=0;
        } else if(X==1 || X==2) {
            flag=1;
        } else if(X==3 && R*C==3) {
            flag=0;
        } else if(X==4 && R*C<=8) {
            flag=0;
        }
        if(flag==1) {
            printf("Case #%d: GABRIEL\n",K);
        } else {
            printf("Case #%d: RICHARD\n",K);
        }
    }
    return 0;
}
