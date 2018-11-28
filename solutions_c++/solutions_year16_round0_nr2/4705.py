#include <bits/stdc++.h>

using namespace std;

const long double INF = INFINITY;
typedef long long ll;
typedef long double ld;

#define s second
#define f first
#define L first
#define R second
#define m0(x) memset(x,0,sizeof(x))
#define pb push_back

#define TASK "problem"

int solve(int t){
    string s;
    cin>>s;
    ll l = s.length(),res = 0,i = l - 1;
    bool f = false;
    char ch;
    for(int k=1;k<=l;k++){
        if(!f) ch = s[i];
        else
            ch = (s[i] == '+' ? '-' : '+');
        if(ch == '-') f = (f ? false : true),res++;
        --i;
    }
    cout<<"Case #"<<t<<": "<<res<<endl;
    return 0;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    freopen(TASK".in","r",stdin);
    freopen(TASK".out","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
        solve(i);

    return 0;
}
