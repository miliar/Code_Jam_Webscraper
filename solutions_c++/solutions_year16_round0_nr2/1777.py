#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define pi pair<ll,ll>
#define pii pair<pi,ll>
#define f first
#define s second
#define ll long long
#define mod 1000000007
#define rep(i,n) for(ll i=0;i<n;i++)
void go(string &s,int i){
    string ans="";
    for(int j=i;j>=0;j--){
        if(s[j]=='+') ans+='-';
        else ans+='+';
    }
    for(int j=i+1;j<s.size();j++){
        ans+=s[j];
    }
    s=ans;
}
int main(){
   freopen("B-large.in","r",stdin);
    freopen("output2.txt","w",stdout);

    int T;
    cin >> T;
    int cur=1;
    while(T--){
        cout<<"Case #"<<cur<<": ";
        cur++;

        int ans=0;

        string s;
        cin  >> s;

        s+='+';
        char p=s[0];
        rep(i,s.size()){
            if(s[i]!=p){
                p=s[i];
                ans++;
            }
        }
        cout<<ans<<"\n";
    }
}
