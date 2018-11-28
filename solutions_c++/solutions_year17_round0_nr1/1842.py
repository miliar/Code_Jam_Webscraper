#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define rep(i,n) for(ll i=0;i<(ll)(n);i++)
#define all(a)  (a).begin(),(a).end()
#define pb emplace_back
#define INF (1e9+1)
//#define INF (1LL<<59)

int main(){
    int n;
    cin>>n;
    
    rep(t,n){
        string s;
        int k;
        cin>>s>>k;
        
        int c=0;
        rep(i,s.size()-k+1){
            if(s[i]=='+')continue;
            c++;
            for(int j=i;j<i+k;j++){
                assert(j<s.size());
                if(s[j]=='-')s[j] = '+';
                else if(s[j]=='+')s[j]='-';
            }
        }
        bool f = false;
        rep(i,s.size()){
            if(s[i]=='-')f|=true;
        }
        cout<<"Case #"<<t+1<<": ";
        if(f)cout<<"IMPOSSIBLE"<<endl;
        else cout<<c<<endl;
    }
}
