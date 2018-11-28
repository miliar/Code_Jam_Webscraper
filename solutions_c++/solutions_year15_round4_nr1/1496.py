#include <bits/stdc++.h>

#define INF (1 << 29)
#define rep2(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) rep2(i,0,n)
#define EPS 1e-10

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

int dx[4] = {-1,0,1,0};
int dy[4] = {0,1,0,-1};

map<char,int> dm;


char check[110][110];

int main()
{
    int T;
    cin >> T;
    dm['v'] = 0;
    dm['>'] = 1;
    dm['^'] = 2;
    dm['<'] = 3;
    rep(case_num,T){
        int r,c;
        cin >> r >> c;
        vector<string> cell(r);
        rep(i,r) cin >> cell[i];
        int res = 0;
        memset(check,0,sizeof(check));
        rep(i,r) {
            int j = 0;
            while(j < cell[i].size() && cell[i][j]=='.') j++;
            if(j<cell[i].size()) check[i][j]|=0x8;
        }
        rep(i,r) {
            int j = cell[i].size()-1;
            while(j >=0 && cell[i][j]=='.') j--;
            if(j>=0) check[i][j]|=0x2;
        }
        rep(j,c){
            int i = 0;
            while(i < r && cell[i][j]=='.') i++;
            if(i<r) check[i][j]|=0x4;
        }
        rep(j,c){
            int i = r-1;
            while(i >= 0 && cell[i][j]=='.') i--;
            if(i>=0) check[i][j]|=0x1;
        }
        rep(i,r) rep(j,c){
            if(check[i][j]==0xf){
                res=-1;
                i = r; j = c;
                break;
            }
            if(cell[i][j]!='.'&&(check[i][j]&(1 << dm[cell[i][j]]))) res++;
        }
        cout << "Case #" << case_num+1 << ": ";
        if(res==-1) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
    }
    return 0;
}

