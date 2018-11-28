#include <cstdio>
#include <iostream>

using namespace std;

int r, c, m;

string ans[10];
int dx[8] = {0,1,0,-1,1,1,-1,-1};
int dy[8] = {1,0,-1,0,1,-1,1,-1};
bool v[5][5];

int check(int ii, int jj){
    int ret = 1;
    v[ii][jj] = true;
    bool flag = false;
    for(int i = 0; i < 8; i++){
        if(ii + dx[i] < 0 || ii + dx[i] >= r)continue;
        if(jj + dy[i] < 0 || jj + dy[i] >= c)continue;
        if(ans[ii + dx[i]][jj + dy[i]] == '*') flag = true;
    }
    if(flag == false){
        for(int i = 0; i < 8; i++){
            if(ii + dx[i] < 0 || ii + dx[i] >= r)continue;
            if(jj + dy[i] < 0 || jj + dy[i] >= c)continue;
            if(!v[ii + dx[i]][jj + dy[i]])
                ret += check(ii + dx[i], jj + dy[i]);
        }
    }
    return ret;
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cin >> r >> c >> m;
        cout << "Case #" << t << ":" << endl;

        for(int i = 0; i < r; i++){
            ans[i] = "";
            for(int j = 0; j < c; j++)
                ans[i] += '!';
        }

        bool flag = false;
        for(int i = 0; i < (1 << (r * c)); i++){
            int cnt = 0;
            for(int j = 0; j < r * c; j++)
                if(i & (1 << j)) cnt++;
            if(cnt != m) continue;
            for(int j = 0; j < r * c; j++)
                if(i & (1 << j)) ans[j / c][j % c] = '*';
                else ans[j / c][j % c] = '.';
            for(int ii = 0; ii < r; ii++)
                for(int jj = 0; jj < c; jj++){
                    if(ans[ii][jj] == '*') continue;
                    memset(v, 0, sizeof(v));
                    if(flag != true && check(ii,jj) == r * c - m){
                        ans[ii][jj] = 'c';
                        flag = true;
                    }
                }
            if(flag == true) break;
        }
        if(flag == false)
            cout << "Impossible" << endl;
        else
            for(int i = 0; i < r; i++)
                cout << ans[i] << endl;
    }
    return 0;
}
