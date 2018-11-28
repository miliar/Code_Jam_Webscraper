#include <bits/stdc++.h>

#define FOR(i,n) for(int i=0;i<n;++i)
#define sz size

using namespace std;

int a[1000];
void solve(string s){
    a[0]=+1;
    FOR(i,s.sz()){
        if(s[i]=='+') a[i+1]=+1;
        else a[i+1]=-1;
    }

    int ans=0;
    int flag=1;
    for(int i=s.sz();i>=1;--i){
        a[0]=1/flag;
        if(a[i]*flag==-1 and a[i-1]*flag==+1){
            ans++;
            flag=-flag;
        }
    }

    cout<<ans<<endl;
}

int main(void){
    int t;cin>>t;
    FOR(i,t){
        string s;cin>>s;
        cout<<"Case #"<<i+1<<": ";
        solve(s);
    }

    return 0;
}
