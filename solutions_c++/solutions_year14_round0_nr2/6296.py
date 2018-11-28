#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    freopen("3.txt","r",stdin);
freopen("4.txt","w",stdout);
    std::ios_base::sync_with_stdio(false);
    int k=0;
    int t;
    cin>>t;
    while(k!=t){
        k++;
        double C,F,X;
        cin>>C>>F>>X;
        double prev=X/2.0;
        double next=C/2.0 + X/(2.0+F);
        double fval=F;
        while(next<prev){
            prev=next;
            next=next-X/(2.0+fval)+C/(2.0+fval)+X/(2.0+fval+F);
            fval+=F;
        }
        printf("Case #%d: %.9lf\n",k,prev);
    }

}
