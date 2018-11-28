#include <bits/stdc++.h>
typedef long long LL;
using namespace std;

using namespace std;
int f(int v,int n){
    //for(int i = 0; i < 10; i++)cout<<(1&(v>>i));cout<<"-"<<n<<"-";
    int u=v;
    for(int i = 0; i < ((n+1)/2); i++){
        if(((v>>i)&1)==((v>>(n-i-1))&1))
            u^=(1<<i)|(1<<(n-i-1));
        }
    //for(int i = 0; i < 10; i++)cout<<(1&(u>>i));cout<<endl;
    return u;
}
void solve(){
    int n;
    queue<int> que;
    map<int,int> used;
    {
        string s;cin>>s;
        n=s.size();
        int t=0;
        for(int i = 0; i < n; i++)
            t|=(s[i]=='-')<<i;
        que.push(t);
        used[t]=0;
    }
    while(used.count(0)==0){
        auto v=que.front();que.pop();
        for(int i = 1; i <= n; i++){
            auto u=f(v,i);
            if(used.count(u))continue;
            used[u]=used[v]+1;
            que.push(u);
        }
    }
    cout<<used[0];
}

int main() {
    int T;cin>>T;
    for(int i = 1; i <= T; i++){
        cout<<"Case #"<<i<<": ";
        solve();
        cout<<endl;
    }

    return 0;
}
