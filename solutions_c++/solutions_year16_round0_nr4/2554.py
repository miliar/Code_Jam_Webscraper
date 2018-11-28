#include<iostream>
#include<string>
#include<sstream>
using namespace std;
int main(){
    int t,cas=0;
    cin>>t;
    while(t--){
        int k,c,s;
        cin>>k>>c>>s;
        cout<<"Case #"<<++cas<<":";
        for(int i=1;i<=k;i++){
            cout<<" "<<i;
        }
        cout<<endl;
    }
}

