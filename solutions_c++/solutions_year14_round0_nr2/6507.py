#include <iostream>
#include <cstdio>
using namespace std;
int a[16];
int b[16];
double ans(double C,double F,double X,double p=2,double n=5000){
    if(n==0)return X/p;
    return min(X/p,C/p+ans(C,F,X,p+F,n-1));
}

int main(){
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,flag;
    cin >> T;
    for(int t=1;t<=T;t++){
        double C,F,X;
        cin >> C >> F >> X;
        printf("Case #%d: %.8lf\n",t,ans(C,F,X));
    }
}
