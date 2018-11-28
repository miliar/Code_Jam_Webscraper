#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>
using namespace std;

int T,S;
string num;

void solve(){
    long sum=num[0]-'0';
    int frd=0;
    for(int i=1;i<num.size();i++){
        while(sum<i){
            frd++;
            sum++;
        }
        sum+=num[i]-'0';
    }
    cout<<frd<<endl;
}

int main(){
    freopen("/Users/caitianchi/Downloads/A-large.in","r",stdin);
    freopen("/Users/caitianchi/Desktop/123.txt","w",stdout);
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>S;
        cin>>num;
        cout<<"Case #"<<i+1<<": ";
        solve();
    }
    return 0;
}



