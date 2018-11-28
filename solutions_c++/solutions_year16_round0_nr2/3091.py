#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;
void solve(){
    int i,c=0;
    string pan;
    cin>>pan;
    pan+='+';
    for(i=0;i<pan.size()-1;i++)
        if(pan[i]!=pan[i+1])
            c++;
    cout<<c<<endl;
}
int main(){
    freopen("pancake.in","r",stdin);
    freopen("pancake.out","w",stdout);
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++){
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}
