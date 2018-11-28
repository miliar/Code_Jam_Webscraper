#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>

using namespace std;


long long int find_rev(long long int t){
    long long int rev;
    rev=0;
    while(t!=0){
            rev=rev*10+t%10;
            t/=10;
        }
    return rev;
}


int main() {
    long long int p,t,T,n,i,d,j,k;
    long long int C[]={0,10,29,138,337,1436,3435,14434,124433,324432,1424431,3424430,14424429,34424428,144424427};
    long long int P[]={1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000};
    cin>>T;
    for(i=1;i<=T;i++){
        cin>>n;
        k=0;
        if(n%10==0){
            k=1;
            t=n-1;
        }
        else t=n;
        d=0;
        while(t!=0){
            d++;
            t/=10;
        }

        k+=C[d-1];
        //cout<<t<<endl;
       // cout<<"n"<<n<<endl;
        if(n%10==0){
            t=n-1;
        }
        else t=n;
       // cout<<t<<endl;
       // cout<<P[d/2+1]<<endl;
        //cout<<find_rev(t/P[d/2+1])<<endl;
        if(d%2==0) k+=find_rev(t/P[d/2] )+t%P[d/2];
        else k+=find_rev(t/P[d/2+1] )+t%P[d/2+1];
        if( find_rev( t/P[d/2] )==1 && d%2==0) k--;
        else if( find_rev( t/P[d/2+1] )==1 && d%2==1) k--;
        cout<<"Case #"<<i<<": "<<k<<endl;
    }
    return 0;
}
