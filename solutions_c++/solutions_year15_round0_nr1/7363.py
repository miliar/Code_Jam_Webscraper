#include <bits/stdc++.h>

#define l(i,n) for(int i=0;i<n;i++)

#define pii pair<int,int>
#define DB()    cout<<"I'm in!"<<endl

typedef long long LL;

using namespace std;


int main(){
std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
    //freopen("A.in","r",stdin);
    //freopen("A.out","w",stdout);
    int t;
    cin>>t;
    l(p,t){
        int n;
        cin>>n;
        string s;
        cin>>s;

        int curr=0;
        int ans=0;

        for(int i=0;i<=n;i++){
            if(curr>=i) curr+=s[i]-'0';
            else{
                ans+=(i-curr);
                curr+=(i-curr);
                curr+=s[i]-'0';
            }
        }
        cout<<"Case #"<<p+1<<": "<<ans<<endl;
    }
return 0;
}
