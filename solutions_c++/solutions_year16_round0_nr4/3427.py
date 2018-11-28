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
    ll k,c,s;
    cin>>k>>c>>s;
    cout<<"Case #"<<t<<": ";
    for(int i=1;i<=s;i++)
        (i==s ? cout<<i : cout<<i<<" ");
    cout<<endl;
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
