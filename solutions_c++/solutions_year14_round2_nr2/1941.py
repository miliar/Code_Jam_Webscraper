#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main(){
    int t,c=1;
    cin>>t;
    int tc=1;
    while(t--){
        int a,b,k;
        cin>>a>>b>>k;
        int count=0;
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++){
                int ans=i&j;
                if(ans<k && ans>=0)  count++;
            }
        }
        cout<<"Case #"<<tc<<": ";
        cout<<count<<endl;
        tc++;
    }
    return 0;
}
