#include <iostream>
#include <algorithm>

using namespace std;
int T;
bool flag[2501];
void solve();
int main(){
    cin>>T;
    for(int i=1;i<=T;++i){
        cout<<"Case #"<<i<<": ";
        solve();
        cout<<endl;
    }
}
void solve(){
    for(int i=0;i<=2500;i++){
        flag[i]=false;
    }
    int N;
    cin>>N;
    for(int j=0;j<2*N-1;++j)
        for(int k=0;k<N;++k){
            int c;
            cin>>c;
            flag[c] = !flag[c];
        }
    for(int i=1;i<=2500;i++)
        if(flag[i])
            cout<<i<<' ';
}
