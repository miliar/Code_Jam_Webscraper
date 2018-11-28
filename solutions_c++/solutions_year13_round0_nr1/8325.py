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
#include <cstring>

using namespace std;

#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i = 0; i < n; i++)
#define rep2(i,v,n) for(int i = (v); i < (n); i++)
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)>(b))?(b):(a))

typedef unsigned long long int ull;
typedef long long int ll;
typedef unsigned int ui;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vector<int> > vvi;
typedef vector<vector<string> > vvs;
int main () {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T;
    vs board;
    cin >> T;
    //cout << T << endl;
    string s;
    int count = 0;
    while (count < T) {
        board.clear();
        count++;
        bool flag = true;
        char winner = 'N';
        rep(i,4) {
            cin >> s;
            board.pb(s);
        }
        // check rows
        rep(i,4) {
            char a = 'T';
            rep(j,4) {
                //cout << board[i][j];
                if (board[i][j] == '.') {flag = false; winner = 'N';break;}
                if (board[i][j] != a) {
                    if (a == 'T') {a = board[i][j]; winner = a;}
                    else if (board[i][j] == 'T');
                    else {winner = 'N'; break; }
                } 
            }
            //cout << endl;
            if (winner != 'N') break;
            
        }
        if (winner == 'N') {
            // check columns
            rep(j,4) {
                char a = 'T';
                rep(i,4) {
                    //cout << board[i][j];
                    if (board[i][j] == '.') {flag = false; winner = 'N';break;}
                    if (board[i][j] != a) {
                        if (a == 'T') {a = board[i][j]; winner = a;}
                        else if (board[i][j] == 'T');
                        else {winner = 'N'; break; }
                    }  
                }
                //cout << endl;
                if (winner != 'N') break;
            }
        }
        if (winner == 'N') {
            // check diagonals
            char a = 'T';
            rep(i,4) {
                
                //cout << board[i][i];
                if (board[i][i] == '.') {flag = false; winner = 'N';break;}
                if (board[i][i] != a) {
                    if (a == 'T') {a = board[i][i];  winner = a;}
                    else if (board[i][i] == 'T');
                    else {winner = 'N'; break; }
                }
            }
            //cout << endl;
            //cout << "winner : " << winner  << endl;
            if (winner == 'N') {
                char a = 'T';
                rep(i,4) {
                    
                    //cout << board[i][3-i];
                    if (board[i][3-i] == '.') {flag = false; winner = 'N';break;}
                    if (board[i][3-i] != a) {
                        if (a == 'T') {a = board[i][3-i];  winner = a;}
                        else if (board[i][3-i] == 'T');
                        else {winner = 'N'; break; }
                    }
                }
                //cout << endl;
            }
            //cout << "winner : " << winner  << endl;
            
        }
        if (winner != 'N') {
            printf("Case #%d: %c won\n", count, winner);
        } 
        else {
            if (flag) printf("Case #%d: Draw\n", count);
            else printf("Case #%d: Game has not completed\n", count);
        }
       
    }
}
