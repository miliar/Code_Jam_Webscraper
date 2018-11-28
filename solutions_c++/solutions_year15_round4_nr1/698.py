#include<bits/stdc++.h>

using namespace std;



void solve(){
    map<char,pair<int,int> > mp;

    mp['.']={0,0};
    mp['^']={-1,0};
    mp['v']={1,0};
    mp['>']={0,1};
    mp['<']={0,-1};
    int n,m;
    cin >> n >> m;
    vector<string> v;
    for(int i = 0 ; i < n ; ++ i ){
        string str;
        cin >> str;
        v.push_back(str);
    }
    vector<int> row(n,0),col(m,0);
    for(int i = 0 ; i < n ; ++ i ){
        for(int j = 0 ; j < m ; ++ j ){
            if(v[i][j]!='.'){
                row[i]++;
                col[j]++;
            }
        }
    }
    for(int i = 0 ; i < n ; ++ i ){
        for(int j = 0 ; j < m ; ++ j ){
            if(row[i]==1&&col[j]==1&&v[i][j]!='.'){
                cout <<"IMPOSSIBLE"<<endl;
                return ;
            }
        }
    }
    int ans = 0;
    for(int i = 0 ; i < n ; ++ i ){
        for(int j = 0 ; j < m ; ++ j ){
            char c=v[i][j];
            int dx,dy;
            dx=mp[c].first;
            dy=mp[c].second;

            if(dx||dy){
                int x=i+dx,y=j+dy;
                while(x>=0&&x<n&&y>=0&&y<m&&v[x][y]=='.'){
                    x+=dx;
                    y+=dy;
                }
                if(x<0||x>=n||y<0||y>=m){
                    ans++;
                }
            }
        }
    }
    cout << ans << endl;

}

int main(){
    freopen("A-large"".in","r",stdin);
    freopen("A-large"".out","w",stdout);
    int T;
    cin >> T;
    for(int i = 1 ; i <= T ; ++ i ){
        cout <<"Case #"<<i<<": ";
        solve();
    }

}
