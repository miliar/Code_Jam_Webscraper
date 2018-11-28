#include<iostream>
using namespace std;
int main(){
 int T,k,c,s;
 cin>>T;
 for(int i=0;i<T;i++){
    cin>>k>>c>>s;
    cout<<"Case #"<<i+1<<": ";
    while(s!=0){
        cout<<s<<" ";
        --s;
    }
    cout<<endl;
 }
}
