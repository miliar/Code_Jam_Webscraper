#include<bits/stdc++.h>
using namespace std;
#define FOR(i,N) for(int i=0; i<N; i++)

int main(){
    int T, R, C;
    cin>>T;
    FOR(tt,T){
        char mp[100][101];
        cin>>R>>C;
        FOR(i,R) cin>>mp[i];
        int ans=0;
        bool ok=true;
        FOR(i,R)FOR(j,C){
            if(mp[i][j] == '.')
                continue;
            int x, y;
            bool u,d,l,r;
            u=d=l=r=false;
            x=i, y=j;
            for(x--; x>=0&&mp[x][y]=='.'; x--);
            if(x<0) u=true;
            x=i, y=j;
            for(x++; x<R&&mp[x][y]=='.'; x++);
            if(x>=R) d=true;
            x=i, y=j;
            for(y--; y>=0&&mp[x][y]=='.'; y--);
            if(y<0) l=true;
            x=i, y=j;
            for(y++; y<C&&mp[x][y]=='.'; y++);
            if(y>=C) r=true;
            if(u&d&l&r) ok = false;
            ans += (mp[i][j]=='^'&&u)|(mp[i][j]=='v'&&d)|(mp[i][j]=='<'&&l)|(mp[i][j]=='>'&&r);
        }
        cout<<"Case #"<<tt+1<<": ";
        if(ok) cout<<ans<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
