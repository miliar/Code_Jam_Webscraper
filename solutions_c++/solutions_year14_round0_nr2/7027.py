#include<iostream>
#include<cstdio>

using namespace std;


int main() {
    freopen("inA.txt","r",stdin);
    freopen("ouA.txt","w",stdout);
    int t;
    cin>>t;
    for(int k=1;k<=t;k++) {
        double a, b, c, d,sum1=0,sum2=0;
        cin>>a>>b>>c;
        if(a/2.0 >= c/2.0)
            printf("Case #%d: %.7f\n",k,c/2.0);
        else {
            d=2.0;
            while(1) {
                sum1=sum1+c/d;
                sum2=sum2+a/d+c/(d+b);
                if(sum1<= sum2) break;
                sum1=sum1-c/d+a/d;

                d=d+b;
                sum2=sum2-c/d;
            }
            printf("Case #%d: %.7f\n",k,sum1);
        }
    }
}
