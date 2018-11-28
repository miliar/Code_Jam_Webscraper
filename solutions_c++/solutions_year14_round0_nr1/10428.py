#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdlib>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define REP(i,j,k) for(int i=j;i<(int)(k);++i)
#define foreach(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef long long ll;
// const int INF = 1 << 29;
// const double EPS = 1e-9;

int T,a0,a1;
int mat[2][4][4];

int main(){
    cin >> T;
    REP(t,1,T+1){
        printf("Case #%d: ",t);
        cin >> a0;
        rep(i,4)rep(j,4) cin >> mat[0][i][j];
        cin >> a1;
        rep(i,4)rep(j,4) cin >> mat[1][i][j];

        a0--; a1--;
        int flag0=0,flag1=0;
        rep(i,4) flag0 |= (1<<mat[0][a0][i]);
        rep(i,4) flag1 |= (1<<mat[1][a1][i]);

        int res = flag0 & flag1;
        int cnt = __builtin_popcount(res);
        if(cnt==0) cout << "Volunteer cheated!";
        else if(cnt>1) cout << "Bad magician!";
        else{
            REP(i,1,17)if(res>>i&1){ cout << i; break; }            
        }
        cout << endl;
    }
    return 0;
}
