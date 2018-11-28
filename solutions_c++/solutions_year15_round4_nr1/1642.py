#include <bits/stdc++.h>
#include<unordered_map>
#include <climits>
#define reset(arr,j) memset(arr,j,sizeof(arr));
#define pb push_back
#define f first
#define s second
#define mp make_pair
#define vec vector<LL>
#define LL long long
#define fa(i,n) for(int i=0;i<n;i++)
#define fb(i,n) for(int i=1;i<=n;i++)
#define take(vec,n) for(int i=0;i<n;i++){int a; cin >> a; vec.pb(a);};
#define print(arr,n) fa(i,n) cout << arr[i] << " "; cout << endl;
#define mod(n,m) (n % m + m) % m;
#define fd(i,n) for(int i=n-1;i>=0;i--)
#define vpair vector < pair <int ,int> >
#define Vec(name,size) vector<int> name(size);
#define matrix vector<vector<LL> >
#define initmatrix(m,a,b,x) fa(i,a){ vector<LL> c; m.pb(c); fa(j,b) m[i].pb(x);};
#define printmatrix(M) fa(i,M.size()){ fa(j,M[i].size()) cout << M[i][j].f <<" "; cout << endl;}
#define O4 10005
#define O5 100006
#define O6 1000005
#define O7 10000007
int dx[] = {0,1,-1,0,1,-1,1,-1,-2,2,0,0},dy[] = {1,0,0,-1,-1,1,1,-1,0,0,-2,2};
using namespace std;
//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//
vector<vector<char> > board;
int R,C;
bool visited[105][105];
bool invalid[105][105];
int ans = 0;
bool run(int x,int y, vector<pair<int,int> > arw,char dir){

    if(x < 0 || x >= R || y < 0 || y >= C){
        if(arw.size() == 1){
            invalid[arw[0].f][arw[0].s] = 1;
            return 0;
        }
        else{
            char inv = board[arw[arw.size()-2].f][arw[arw.size()-2].s];
            if(inv == '^')
                board[arw[arw.size()-1].f][arw[arw.size()-1].s] = 'v';
            else if(inv == 'v')
                board[arw[arw.size()-1].f][arw[arw.size()-1].s] = '^';
            else if(inv == '>')
                board[arw[arw.size()-1].f][arw[arw.size()-1].s] = '<';
            else if(inv == '<')
                board[arw[arw.size()-1].f][arw[arw.size()-1].s] = '>';
            invalid[arw[arw.size()-1].f][arw[arw.size()-1].s] = 0;
            ans++;
            return 1;
        }
    }

    if(dir == '.'){
        return 1;
    }

    if(visited[x][y])
        return 1;

    visited[x][y] = 1;

    vector<pair<int,int> > arr = arw;
    if(board[x][y] != '.'){
        dir = board[x][y];
        arr.pb(mp(x,y));
    }


    if(dir == '>'){
        return run(x,y+1,arr,dir);
    }
    if(dir == 'v'){
        return run(x+1,y,arr,dir);
    }
    if(dir == '<'){
        return run(x,y-1,arr,dir);
    }
    if(dir == '^'){
        return run(x-1,y,arr,dir);
    }

}
main(){
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin >> T;
    for(int t = 1;t <= T;t++){
        ans = 0;
        cin >> R >> C;
        board = vector<vector<char> > (R, vector<char> (C));
        fa(i,R)
            fa(j,C)
                cin >> board[i][j];
        reset(visited,0);
        reset(invalid,0);
        bool ok = 1;
        int arrs = 0;
        fa(i,R) fa(j,C){
                run(i,j,vector<pair<int,int> >(),board[i][j]);
                if(board[i][j] != '.')
                    arrs++;
                reset(visited,0);
        }
//        fa(i,R){
//            fa(j,C){
//                cout << board[i][j];
//            }
//            cout << endl;
//        }
        fa(i,R) fa(j,C){
            if(invalid[i][j]){
                board[i][j] = '>';
                bool right = run(i,j,vector<pair<int,int> >(),'>');
                reset(visited,0);
                board[i][j] = '^';
                bool up = run(i,j,vector<pair<int,int> >(),'^');
                reset(visited,0);
                board[i][j] = 'v';
                bool down = run(i,j,vector<pair<int,int> >(),'V');
                reset(visited,0);
                board[i][j] = '<';
                bool left = run(i,j,vector<pair<int,int> >(),'<');
                reset(visited,0);
                if(right)
                    board[i][j] = '>';
                if(left)
                    board[i][j] = '<';
                if(up)
                    board[i][j] = '^';
                if(down)
                    board[i][j] = 'v';
                if(right || up || down || left){
                    ans = min(ans+1,arrs);
                }
                else{
                    ok = 0;
                }
            }
        }
        printf("Case #%d: ",t);
        if(ok)
            cout << ans << endl;
        else
            cout << "IMPOSSIBLE\n";
    }
}
