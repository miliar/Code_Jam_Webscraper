#include<iostream>
#include<vector>
#include<string>
#include<fstream>

using namespace std;

int main() {
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t; cin>>t;
    for(int T = 1; T <= t;T++) {
        int a,b,k; cin>>a>>b>>k;
        int cnt = 0;
        for(int i = 0;i < a;i++) {
            for(int j  = 0;j < b;j++) {
                //cout<<i<<' '<<j<<' '<<(i & j)<<endl;
                if((i & j) < k) {cnt++;}
            }
        }
        cout<<"Case #"<<T<<": "<<cnt<<endl;
    }
}
