#include <bits/stdc++.h>                 
using namespace std;                     
using ll = long long;                    
using vl = vector<ll>;                   
using vvl = vector<vl>;                  
using pll = pair<ll,ll>;                 
using vb = vector<bool>;                 
const ll oo = 0x3f3f3f3f3f3f3f3fLL;      
const double eps = 1e-9;                 
#define sz(c) ll((c).size())             
#define all(c) begin(c),end(c)           
#define mp make_pair                     
#define mt make_tuple                    
#define pb push_back                     
#define eb emplace_back                  
#define xx first                         
#define yy second                       
#define has(c,i) ((c).find(i) != end(c))
#define FOR(i,a,b) for (int i=(a); i<(b); i++)       
#define FORD(i,a,b) for (int i=int(b)-1; i>=(a); i--)
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

static ll target[100][100][4];
static char field[100][100];

static ll R, C;

static unordered_map<char,int> dm {{'>',1},{'<',0},{'^',2},{'v',3}};

int main() { ios::sync_with_stdio(false);
    ll T;
    cin >> T;
    FOR(tc,1,T+1) {
        cin >> R >> C;
        FOR(r,0,R) FOR(c,0,C)
            cin >> field[r][c];
        FOR(r,0,R) {
            ll lasttarget = -1;
            FOR(c,0,C) {
                target[r][c][0] = lasttarget;
                if(field[r][c] != '.') lasttarget = c;
            }
        }
        FOR(r,0,R) {
            ll lasttarget = -1;
            FORD(c,0,C) {
                target[r][c][1] = lasttarget;
                if(field[r][c] != '.') lasttarget = c;
            }
        }
        FOR(c,0,C) {
            ll lasttarget = -1;
            FOR(r,0,R) {
                target[r][c][2] = lasttarget;
                if(field[r][c] != '.') lasttarget = r;
            }
        }
        FOR(c,0,C) {
            ll lasttarget = -1;
            FORD(r,0,R) {
                target[r][c][3] = lasttarget;
                if(field[r][c] != '.') lasttarget = r;
            }
        }
        ll res = 0;
        bool possible = true;
        FOR(r,0,R) FOR(c,0,C) if(field[r][c] != '.' && target[r][c][dm[field[r][c]]] == -1) {
            FOR(i,0,5) {
                if(i == 4) {possible = false; break;}
                if(target[r][c][i] != -1) {++res; break;}
            }
        }
        cout << "Case #" << tc << ": ";
        if(possible) cout << res;
        else cout << "IMPOSSIBLE";
        cout << endl;
    }
}
