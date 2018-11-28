#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

typedef long long  LL;

int C,K,S;
vector<LL> ans;
LL dx[128];

LL dfs(int mark,int h){
    if(h==C || mark==K) return 1LL;
    return dx[C-1-h]*(LL)mark + dfs(mark+1,h+1);
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        cin>>K>>C>>S;
        int min_need = (K+C-1)/C;
        if(min_need>S) ans.clear();
        else{
            ans.resize(min_need);
            dx[0] = 1LL;
            for(int i=1;i<C;i++) dx[i]=dx[i-1]*(LL)K;

            for(int i=0;i<min_need;i++){
                ans[i] = dfs(i*C,0);
            }

        }
        printf("Case #%d:",cas);
        if(ans.size()>0){
            for(LL elem:ans) cout<<" "<<elem;cout<<endl;
        }
        else cout<<" IMPOSSIBLE"<<endl;

    }
    return 0;
}
