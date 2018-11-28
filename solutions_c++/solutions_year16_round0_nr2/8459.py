#include<bits/stdc++.h>
using namespace std;
#define ll int
#define sc second
#define fr first
#define pb push_back
#define ARRS int(2e5+10)
#define INF int(2e8+10)


int main(){
    #ifdef KHOKHO
        freopen("in.in","r",stdin);
        freopen("out.out","w+",stdout);
    #endif
    ll m;
    cin>>m;
    for(int t=1; t<=m; t++){
        string s;
        cin>>s;
        ll n;
        n=s.size();
        ll pas=0;
        pas=1;
        for(int i=1; i<n; i++){
            if(s[i]!=s[i-1])
                pas++;
        }
        if(s[n-1]=='+')
            pas--;
        cout<<"Case #"<<t<<": "<<pas<<endl;
    }
    return 0;
}
