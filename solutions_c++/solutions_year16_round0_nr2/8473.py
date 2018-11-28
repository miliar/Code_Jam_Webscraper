#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
long long n,m,k,l,i,j,a,b,t,d[15],res;

int main() {
    
    cin>>t;
    while(t--){
        cin>>n;
        res=0;
        l=0;
        j++;
        cout<<"case #"<<j<<": ";
        if(n==0) {cout<<"INSOMNIA\n";continue;}
        while(1){
            l+=n;
            k=l;
            while(k>=1){
                if(d[k%10]==0) {res++;d[k%10]=1;}
                k/=10;
                
            }
            if(res==10) {cout<<l<<endl;break;}
       //     cout<<res<<" ";
        }
        for(i=0;i<10;i++){
            d[i]=0;
        }
    }
    return 0;
}
