#include <bits/stdc++.h>
#define sz(x) ((int)(x).size())
#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define repsz(i,v) rep(i,sz(v))
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fst first
#define snd second
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define bit(x) (1LL<<(x))
#define int long long
#define cauto const auto &
static const int INF = 1<<25;
static const double EPS = 1e-5;
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
template<class T> T mineq(T &a, const T &b){ return a = min(a, b); }
template<class T> T maxeq(T &a, const T &b){ return a = max(a, b); }
template<typename T> T s_to(string s){ //{{{
    stringstream ss;
    T res;
    ss << s;
    ss >> res;
    return res;
} //}}}

constexpr array<int, 8> dx = {{+1,  0, -1,  0, +1, +1, -1, -1}};
constexpr array<int, 8> dy = {{ 0, +1,  0, -1, +1, -1, +1, -1}};

int in(const vvi &board, int i, int j){
    const auto &h = sz(board), &w = sz(board[0]);
    return 0 <= i && i < h && 0 <= j && j < w;
}
int get(const vvi &board, int i, int j){
    if(!in(board, i, j)) return 0;
    return board[i][j];
}
int open(vvi &board, int i, int j){
    if(board[i][j]) return 0;
    const auto &h = sz(board), &w = sz(board[0]);
    vvi used(h, vi(w, 0)); used[i][j] = 1;
    queue<tuple<int, int>> q; q.push(mt(i, j));
    int res = 0;
    while(!q.empty()){
        int x = get<0>(q.front()), y = get<1>(q.front()); q.pop();
        int cnt = 0;
        rep(dir, 8) if(get(board, x+dx[dir], y+dy[dir])) ++cnt;
        if(cnt == 0) rep(dir, 8){
            int nx = x + dx[dir], ny = y + dy[dir];
            if(in(board, nx, ny) && !used[nx][ny]){
                used[nx][ny] = 1;
                q.push(mt(nx, ny));
            }
        }
        ++res;
    }
    return res;
}

void solve(int h, int w, int m, ostream &os){//{{{
    if(m == 0){
        rep(i, h){
            rep(j, w){
                if(i == 0 && j == 0) os << 'c';
                else os << '.';
            }
            os << endl;
        }
        return;
    }

    vvi board(h, vi(w));
    for(int A = bit(m)-1; A < bit(h*w); ){
        rep(i, h) rep(j, w) board[i][j] = (A&bit(i*w+j)) != 0;
        rep(i, h) rep(j, w) if(h*w-m == open(board, i, j)){
            rep(a, h){
                rep(b, w){
                    if(a == i && b == j){
                        os << 'c';
                    }else{
                        os << (board[a][b] ? '*' : '.');
                    }
                }
                os << endl;
            }
            return;
        }

        int Ax = A&-A, Ay = A+Ax;
        A = ((A&~Ay)/Ax>>1) | Ay;
    }
    os << "Impossible" << endl;
}//}}}

vector<string> split(const string &s, const char &del){ //{{{
    vector<string> res;
    int p = 0, q;
    while((q = s.find_first_of(del, p)) != string::npos){
        res.pb(s.substr(p, q-p));
        p = q+1;
    }
    res.pb(s.substr(p));
    return res;
} //}}}
void precalc(){//{{{
    for(int r = 1; r <= 5; ++r) for(int c = 1; c <= 5; ++c) for(int m = 0; m < r*c; ++m){
        stringstream ss;
        solve(r, c, m, ss);
        cout << "ans[" << r << "][" << c << "][" << m << "] = \"";
        vector<string> t = split(ss.str(), '\n');
        for(cauto s : t){
            cout << s;
            if(s != "") cout << "\\n";
        }
        cout << "\";" << endl;
    }
}//}}}

string ans[10][10][100];
void pre(){//{{{
    ans[1][1][0] = "c\n";
    ans[1][2][0] = "c.\n";
    ans[1][2][1] = "*c\n";
    ans[1][3][0] = "c..\n";
    ans[1][3][1] = "*.c\n";
    ans[1][3][2] = "**c\n";
    ans[1][4][0] = "c...\n";
    ans[1][4][1] = "*.c.\n";
    ans[1][4][2] = "**.c\n";
    ans[1][4][3] = "***c\n";
    ans[1][5][0] = "c....\n";
    ans[1][5][1] = "*.c..\n";
    ans[1][5][2] = "**.c.\n";
    ans[1][5][3] = "***.c\n";
    ans[1][5][4] = "****c\n";
    ans[2][1][0] = "c\n.\n";
    ans[2][1][1] = "*\nc\n";
    ans[2][2][0] = "c.\n..\n";
    ans[2][2][1] = "Impossible\n";
    ans[2][2][2] = "Impossible\n";
    ans[2][2][3] = "**\n*c\n";
    ans[2][3][0] = "c..\n...\n";
    ans[2][3][1] = "Impossible\n";
    ans[2][3][2] = "*.c\n*..\n";
    ans[2][3][3] = "Impossible\n";
    ans[2][3][4] = "Impossible\n";
    ans[2][3][5] = "***\n**c\n";
    ans[2][4][0] = "c...\n....\n";
    ans[2][4][1] = "Impossible\n";
    ans[2][4][2] = "*.c.\n*...\n";
    ans[2][4][3] = "Impossible\n";
    ans[2][4][4] = "**.c\n**..\n";
    ans[2][4][5] = "Impossible\n";
    ans[2][4][6] = "Impossible\n";
    ans[2][4][7] = "****\n***c\n";
    ans[2][5][0] = "c....\n.....\n";
    ans[2][5][1] = "Impossible\n";
    ans[2][5][2] = "*.c..\n*....\n";
    ans[2][5][3] = "Impossible\n";
    ans[2][5][4] = "**.c.\n**...\n";
    ans[2][5][5] = "Impossible\n";
    ans[2][5][6] = "***.c\n***..\n";
    ans[2][5][7] = "Impossible\n";
    ans[2][5][8] = "Impossible\n";
    ans[2][5][9] = "*****\n****c\n";
    ans[3][1][0] = "c\n.\n.\n";
    ans[3][1][1] = "*\n.\nc\n";
    ans[3][1][2] = "*\n*\nc\n";
    ans[3][2][0] = "c.\n..\n..\n";
    ans[3][2][1] = "Impossible\n";
    ans[3][2][2] = "**\n..\nc.\n";
    ans[3][2][3] = "Impossible\n";
    ans[3][2][4] = "Impossible\n";
    ans[3][2][5] = "**\n**\n*c\n";
    ans[3][3][0] = "c..\n...\n...\n";
    ans[3][3][1] = "*.c\n...\n...\n";
    ans[3][3][2] = "Impossible\n";
    ans[3][3][3] = "***\n...\nc..\n";
    ans[3][3][4] = "Impossible\n";
    ans[3][3][5] = "***\n*..\n*.c\n";
    ans[3][3][6] = "Impossible\n";
    ans[3][3][7] = "Impossible\n";
    ans[3][3][8] = "***\n***\n**c\n";
    ans[3][4][0] = "c...\n....\n....\n";
    ans[3][4][1] = "*.c.\n....\n....\n";
    ans[3][4][2] = "**.c\n....\n....\n";
    ans[3][4][3] = "*.c.\n*...\n*...\n";
    ans[3][4][4] = "****\n....\nc...\n";
    ans[3][4][5] = "Impossible\n";
    ans[3][4][6] = "****\n*...\n*.c.\n";
    ans[3][4][7] = "Impossible\n";
    ans[3][4][8] = "****\n**..\n**.c\n";
    ans[3][4][9] = "Impossible\n";
    ans[3][4][10] = "Impossible\n";
    ans[3][4][11] = "****\n****\n***c\n";
    ans[3][5][0] = "c....\n.....\n.....\n";
    ans[3][5][1] = "*.c..\n.....\n.....\n";
    ans[3][5][2] = "**.c.\n.....\n.....\n";
    ans[3][5][3] = "***.c\n.....\n.....\n";
    ans[3][5][4] = "**.c.\n*....\n*....\n";
    ans[3][5][5] = "*****\n.....\nc....\n";
    ans[3][5][6] = "**.c.\n**...\n**...\n";
    ans[3][5][7] = "*****\n*....\n*.c..\n";
    ans[3][5][8] = "Impossible\n";
    ans[3][5][9] = "*****\n**...\n**.c.\n";
    ans[3][5][10] = "Impossible\n";
    ans[3][5][11] = "*****\n***..\n***.c\n";
    ans[3][5][12] = "Impossible\n";
    ans[3][5][13] = "Impossible\n";
    ans[3][5][14] = "*****\n*****\n****c\n";
    ans[4][1][0] = "c\n.\n.\n.\n";
    ans[4][1][1] = "*\n.\nc\n.\n";
    ans[4][1][2] = "*\n*\n.\nc\n";
    ans[4][1][3] = "*\n*\n*\nc\n";
    ans[4][2][0] = "c.\n..\n..\n..\n";
    ans[4][2][1] = "Impossible\n";
    ans[4][2][2] = "**\n..\nc.\n..\n";
    ans[4][2][3] = "Impossible\n";
    ans[4][2][4] = "**\n**\n..\nc.\n";
    ans[4][2][5] = "Impossible\n";
    ans[4][2][6] = "Impossible\n";
    ans[4][2][7] = "**\n**\n**\n*c\n";
    ans[4][3][0] = "c..\n...\n...\n...\n";
    ans[4][3][1] = "*.c\n...\n...\n...\n";
    ans[4][3][2] = "*.c\n*..\n...\n...\n";
    ans[4][3][3] = "***\n...\nc..\n...\n";
    ans[4][3][4] = "***\n*..\n..c\n...\n";
    ans[4][3][5] = "Impossible\n";
    ans[4][3][6] = "***\n***\n...\nc..\n";
    ans[4][3][7] = "Impossible\n";
    ans[4][3][8] = "***\n***\n*..\n*.c\n";
    ans[4][3][9] = "Impossible\n";
    ans[4][3][10] = "Impossible\n";
    ans[4][3][11] = "***\n***\n***\n**c\n";
    ans[4][4][0] = "c...\n....\n....\n....\n";
    ans[4][4][1] = "*.c.\n....\n....\n....\n";
    ans[4][4][2] = "**.c\n....\n....\n....\n";
    ans[4][4][3] = "**.c\n*...\n....\n....\n";
    ans[4][4][4] = "****\n....\nc...\n....\n";
    ans[4][4][5] = "****\n*...\n..c.\n....\n";
    ans[4][4][6] = "****\n**..\n...c\n....\n";
    ans[4][4][7] = "****\n*...\n*.c.\n*...\n";
    ans[4][4][8] = "****\n****\n....\nc...\n";
    ans[4][4][9] = "Impossible\n";
    ans[4][4][10] = "****\n****\n*...\n*.c.\n";
    ans[4][4][11] = "Impossible\n";
    ans[4][4][12] = "****\n****\n**..\n**.c\n";
    ans[4][4][13] = "Impossible\n";
    ans[4][4][14] = "Impossible\n";
    ans[4][4][15] = "****\n****\n****\n***c\n";
    ans[4][5][0] = "c....\n.....\n.....\n.....\n";
    ans[4][5][1] = "*.c..\n.....\n.....\n.....\n";
    ans[4][5][2] = "**.c.\n.....\n.....\n.....\n";
    ans[4][5][3] = "***.c\n.....\n.....\n.....\n";
    ans[4][5][4] = "***.c\n*....\n.....\n.....\n";
    ans[4][5][5] = "*****\n.....\nc....\n.....\n";
    ans[4][5][6] = "*****\n*....\n..c..\n.....\n";
    ans[4][5][7] = "*****\n**...\n...c.\n.....\n";
    ans[4][5][8] = "*****\n***..\n....c\n.....\n";
    ans[4][5][9] = "*****\n**...\n*..c.\n*....\n";
    ans[4][5][10] = "*****\n*****\n.....\nc....\n";
    ans[4][5][11] = "*****\n**...\n**.c.\n**...\n";
    ans[4][5][12] = "*****\n*****\n*....\n*.c..\n";
    ans[4][5][13] = "Impossible\n";
    ans[4][5][14] = "*****\n*****\n**...\n**.c.\n";
    ans[4][5][15] = "Impossible\n";
    ans[4][5][16] = "*****\n*****\n***..\n***.c\n";
    ans[4][5][17] = "Impossible\n";
    ans[4][5][18] = "Impossible\n";
    ans[4][5][19] = "*****\n*****\n*****\n****c\n";
    ans[5][1][0] = "c\n.\n.\n.\n.\n";
    ans[5][1][1] = "*\n.\nc\n.\n.\n";
    ans[5][1][2] = "*\n*\n.\nc\n.\n";
    ans[5][1][3] = "*\n*\n*\n.\nc\n";
    ans[5][1][4] = "*\n*\n*\n*\nc\n";
    ans[5][2][0] = "c.\n..\n..\n..\n..\n";
    ans[5][2][1] = "Impossible\n";
    ans[5][2][2] = "**\n..\nc.\n..\n..\n";
    ans[5][2][3] = "Impossible\n";
    ans[5][2][4] = "**\n**\n..\nc.\n..\n";
    ans[5][2][5] = "Impossible\n";
    ans[5][2][6] = "**\n**\n**\n..\nc.\n";
    ans[5][2][7] = "Impossible\n";
    ans[5][2][8] = "Impossible\n";
    ans[5][2][9] = "**\n**\n**\n**\n*c\n";
    ans[5][3][0] = "c..\n...\n...\n...\n...\n";
    ans[5][3][1] = "*.c\n...\n...\n...\n...\n";
    ans[5][3][2] = "*.c\n*..\n...\n...\n...\n";
    ans[5][3][3] = "***\n...\nc..\n...\n...\n";
    ans[5][3][4] = "***\n*..\n..c\n...\n...\n";
    ans[5][3][5] = "***\n*..\n*.c\n...\n...\n";
    ans[5][3][6] = "***\n***\n...\nc..\n...\n";
    ans[5][3][7] = "***\n***\n*..\n..c\n...\n";
    ans[5][3][8] = "Impossible\n";
    ans[5][3][9] = "***\n***\n***\n...\nc..\n";
    ans[5][3][10] = "Impossible\n";
    ans[5][3][11] = "***\n***\n***\n*..\n*.c\n";
    ans[5][3][12] = "Impossible\n";
    ans[5][3][13] = "Impossible\n";
    ans[5][3][14] = "***\n***\n***\n***\n**c\n";
    ans[5][4][0] = "c...\n....\n....\n....\n....\n";
    ans[5][4][1] = "*.c.\n....\n....\n....\n....\n";
    ans[5][4][2] = "**.c\n....\n....\n....\n....\n";
    ans[5][4][3] = "**.c\n*...\n....\n....\n....\n";
    ans[5][4][4] = "****\n....\nc...\n....\n....\n";
    ans[5][4][5] = "****\n*...\n..c.\n....\n....\n";
    ans[5][4][6] = "****\n**..\n...c\n....\n....\n";
    ans[5][4][7] = "****\n**..\n*..c\n....\n....\n";
    ans[5][4][8] = "****\n****\n....\nc...\n....\n";
    ans[5][4][9] = "****\n****\n*...\n..c.\n....\n";
    ans[5][4][10] = "****\n****\n**..\n...c\n....\n";
    ans[5][4][11] = "****\n****\n*...\n*.c.\n*...\n";
    ans[5][4][12] = "****\n****\n****\n....\nc...\n";
    ans[5][4][13] = "Impossible\n";
    ans[5][4][14] = "****\n****\n****\n*...\n*.c.\n";
    ans[5][4][15] = "Impossible\n";
    ans[5][4][16] = "****\n****\n****\n**..\n**.c\n";
    ans[5][4][17] = "Impossible\n";
    ans[5][4][18] = "Impossible\n";
    ans[5][4][19] = "****\n****\n****\n****\n***c\n";
    ans[5][5][0] = "c....\n.....\n.....\n.....\n.....\n";
    ans[5][5][1] = "*.c..\n.....\n.....\n.....\n.....\n";
    ans[5][5][2] = "**.c.\n.....\n.....\n.....\n.....\n";
    ans[5][5][3] = "***.c\n.....\n.....\n.....\n.....\n";
    ans[5][5][4] = "***.c\n*....\n.....\n.....\n.....\n";
    ans[5][5][5] = "*****\n.....\nc....\n.....\n.....\n";
    ans[5][5][6] = "*****\n*....\n..c..\n.....\n.....\n";
    ans[5][5][7] = "*****\n**...\n...c.\n.....\n.....\n";
    ans[5][5][8] = "*****\n***..\n....c\n.....\n.....\n";
    ans[5][5][9] = "*****\n***..\n*...c\n.....\n.....\n";
    ans[5][5][10] = "*****\n*****\n.....\nc....\n.....\n";
    ans[5][5][11] = "*****\n*****\n*....\n..c..\n.....\n";
    ans[5][5][12] = "*****\n*****\n**...\n...c.\n.....\n";
    ans[5][5][13] = "*****\n*****\n***..\n....c\n.....\n";
    ans[5][5][14] = "*****\n*****\n**...\n*..c.\n*....\n";
    ans[5][5][15] = "*****\n*****\n*****\n.....\nc....\n";
    ans[5][5][16] = "*****\n*****\n**...\n**.c.\n**...\n";
    ans[5][5][17] = "*****\n*****\n*****\n*....\n*.c..\n";
    ans[5][5][18] = "Impossible\n";
    ans[5][5][19] = "*****\n*****\n*****\n**...\n**.c.\n";
    ans[5][5][20] = "Impossible\n";
    ans[5][5][21] = "*****\n*****\n*****\n***..\n***.c\n";
    ans[5][5][22] = "Impossible\n";
    ans[5][5][23] = "Impossible\n";
    ans[5][5][24] = "*****\n*****\n*****\n*****\n****c\n";
}//}}}

void solve(){
    int h, w, m; cin >> h >> w >> m;
    cout << ans[h][w][m];
}
signed main(){
    //precalc();
    //return 0;
    //cin.tie(0);
    //ios_base::sync_with_stdio(0);
    pre();
    cout.setf(ios::fixed); cout.precision(10);
    string s;
    getline(cin, s);
    int T = s_to<int>(s);
    rep(i, T){
        cout << "Case #" << (i+1) << ":" << endl;
        solve();
    }
    return 0;
}
/* vim:set foldmethod=marker commentstring=//%s : */
