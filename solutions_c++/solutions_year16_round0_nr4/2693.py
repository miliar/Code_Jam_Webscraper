#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int main(){
    //freopen("d.in","r",stdin);
    //freopen("d.out","w",stdout);
    int T,ca=0;
    long long c,k,s;
    cin>>T;
    while(T--){
        ca++;
        cin>>k>>c>>s;
        long long t=1;
        for(int i=1;i<c;i++){
            t*=k;
        }
        cout<<"Case #"<<ca<<":";
        for(long long i=1;i<=s;i++){
            cout<<" "<<(i-1)*t+1;
        }
        cout<<endl;
    }
    return 0;
}
