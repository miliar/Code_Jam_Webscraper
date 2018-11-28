#include<bits/stdc++.h>
using namespace std;
void ins(long long n,set<int> &st){
    while(n>0){
        st.insert(n%10);
        n/=10;
    }
    return;
}
int main(){
    int t;
    //ios::sync_with_stdio("false");
    //stringstream ss;
    cin>>t;
    for(int tt=1;tt<=t;tt++){
        cout<<"Case #"<<tt<<": ";
        long long n,ans;
        cin>>n;
        if(n==0){
            cout<<"INSOMNIA\n";
            continue;
        }
        set<int>st;
        ans=0;
        while(st.size()!=10){
            ans+=n;
            ins(ans,st);
        }
        cout<<ans<<endl;
    }
}
