#include<iostream>
#include<math.h>
#include<algorithm>
#include<sstream>
using namespace std;


int main(){
    int t;
    cin>>t;
    int n=t;
    while(t--){
        cout<<"Case #"<<n-t<<": ";
        long long int a,b;
        cin>>a>>b;
        int count=0;
        long long int ret[]={1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404};
        for(int i=0;i<21;i++){
            if(ret[i]>=a and ret[i]<=b)count++;
        }
        cout<<count<<"\n";
    }
    return 0;
}








