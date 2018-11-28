#include <stdio.h>
#include <iostream>
using namespace std;
int main(){
    long long tt,TT,i,d;
    long long n,p,s,A,B;
    cin >> TT;
    for( tt=0; tt<TT; tt++ ){
        cin >> n >> p;
        if(p==(1LL<<n)){
            A=B=p-1;
        }else{
            p--;
            s=0;
            d=0;
            for( i=n-1; i>=0; i-- ){
                s+=(1LL<<i);
                d++;
                if(s>p) break;
            }
            A=(1LL<<d)-2;

            p=(1LL<<n)-p-2;
            s=0;
            d=0;
            for( i=n-1; i>=0; i-- ){
                s+=(1LL<<i);
                d++;
                if(s>p) break;
            }
            B=(1LL<<n)-2-((1LL<<d)-2);
        }
        cout << "Case #" << tt+1 << ": " << A << " " << B <<endl;
    }
    return 0;
}
