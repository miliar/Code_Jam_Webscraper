#include<iostream>
#include<cstdio>
#include<algorithm>
#include<iterator>
#include<vector>
#include<set>
typedef long long ll;
using namespace std;
int main(){
    int nn;
    cin>>nn;
    for(int t=0;t<nn;t++){
        ll a,b,k;
        ll res=0;
        cin>>a>>b>>k;
        //Magic
        for(ll i =0;i<a;++i){
            for(ll j =0;j<b;++j){
                if((i&j)<k) ++res;
            }
        }
        cout<<"Case #"<<t+1<<": ";
        cout<<res;
        cout<<endl;
    }
}

