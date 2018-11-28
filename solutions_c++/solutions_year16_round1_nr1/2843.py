#include "bits/stdc++.h"
#include <cassert>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define vi vector<int>
#define pb push_back
#define INF 999999999
//#define INF (1LL<<59)

int main(){
    int t;
    cin>>t;
    rep(loop,t){
        string s;
        cin>>s;
        
        string ans = "";
        rep(i,s.size()){
            if(ans.size()==0||ans[0]<=s[i]){
                ans = s[i]+ans;
            }
            else{
                ans+=s[i];
            }
        }
        cout<<"Case #"<<loop+1<<": ";
        cout<<ans<<endl;
    }
}