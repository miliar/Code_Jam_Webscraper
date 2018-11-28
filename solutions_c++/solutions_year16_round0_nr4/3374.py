#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){

int t;
cin>>t;
int k , c,s,i=0;
while(t--){
    cout<<"Case #"<<++i<<": ";
    cin>>k>>c>>s;
    if(c==1) {
        if(s<k) cout<<"IMPOSIBLE"<<endl;
        else {
            for(int i=1;i<=k;i++) cout<<i<<" ";
            cout<<endl;
        }
    }
   else if(s<k-1)cout<<"IMPOSIBLE"<<endl;
    else {
        for(int i=2;i<=k;i++) cout<<i<<" ";
            cout<<endl;
    }
}
}
