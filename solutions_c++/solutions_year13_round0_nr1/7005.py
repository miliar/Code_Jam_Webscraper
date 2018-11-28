#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

#define INF                         (int)1e9
#define EPS                         1e-9

#define bitcount                    __builtin_popcount
#define gcd                         __gcd

#define FOR(i,a,b)                  for(int i=a;i<b;i++)
#define REP(i,a)                    FOR(i, 0, a)
#define FOREACH(v, c)               for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define all(a)                      a.begin(), a.end()
#define SORT(a)                     sort(all(a))
#define in(a,b)                     ( (b).find(a) != (b).end())
#define pb                          push_back
#define fill(a,v)                   memset(a, v, sizeof a)
#define sz(a)                       ((int)(a.size()))
#define mp                          make_pair
#define vout(x)                     FOREACH(_i, x) cout<< *_i << " "; cout << endl;
#define debug(x)                    cout << #x << " : " << x << endl;
#define checkbit(n,b)               ( (n >> b) & 1)
#define DREP(a)                     sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind)              (lower_bound(all(arr),ind)-arr.begin())
#define LL                          long long
#define LD                          long double
#define VI                          vector<int>
#define VVI                         vector<VI>
#define VS                          vector<string>
#define PII                         pair<int,int>
#define VII                         vector<PII>

using namespace std;


bool is_winner(VS &board, char player){
    // Row wise
    FOR(i, 0, 4){
        int row_count = 0;
        FOR(j, 0, 4){
            if(board[i][j] == player || board[i][j] == 'T')
                row_count++;
        }
        if(row_count == 4){
            return true;
        }
    }

    // Column wise
    FOR(i, 0, 4){
        int col_count = 0;
        FOR(j, 0, 4){
            if(board[j][i] == player || board[j][i] == 'T')
                col_count++;
        }
        if(col_count == 4){
            return true;
        }
    }

    // Diagonals
    int primary = 0, secondary = 0;
    FOR(i, 0, 4){
        if(board[i][i] == player || board[i][i] == 'T')
            primary++;
        if(board[i][4-i-1] == player || board[i][4-i-1] == 'T')
            secondary++;
    }
    if(primary == 4 || secondary == 4)
        return true;

    return false;
}

string get_winner(VS &board){
    if(is_winner(board, 'X'))
        return "X won";
    else if(is_winner(board, 'O'))
        return "O won";

    FOR(i, 0, 4){
        FOR(j, 0, 4){
            if(board[i][j] == '.')
                return "Game has not completed";
        }
    }

    return "Draw";
}

int main(){
    int T;
    cin >> T;
    FOR(tc, 1, T+1){
        cin.ignore();
        VS board;
        string s;
        FOR(i, 0, 4){
            cin >> s;
            board.pb(s);
        }
        cout << "Case #"<< tc << ": " << get_winner(board) << endl;
    }
    return 0;
}