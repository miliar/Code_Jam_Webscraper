/* Paras Narang */
#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <deque>
#include <bitset>
#include <cmath>
#include <set>
#include <sstream>

using namespace std;

#define oo 0x7F7F7F7F
#define LET(x,a)     __typeof(a) x(a)
#define EACH(it,v)   for(LET(it,v.begin());it!=v.end();++it)
#define FOR(i,a,b)   for(__typeof(b) i(a); i<b; i++)
#define REP(i,n)     for(__typeof(n) i(0); i<n; i++)
#define ALL(x)       (x).begin(), (x).end()
#define gint(t)      scanf("%d", &t);
#define pint(t)      printf("%d\n", t);
#define pb           push_back
#define mp           make_pair

typedef long long int   ll;
typedef unsigned long long int ull;
typedef unsigned int    uint;
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector<vi>      vii;
typedef vector<pii>     vpii;

int main(){
    int T; gint(T);
    REP(ti, T){
        char ch;
        int game[4][4], emptySlotFlag = 0, xWon = 0, oWon = 0;
        int colSum[4] = {0, 0, 0, 0}, rowSum[4] = {0, 0, 0, 0}, diaSum[2] = {0, 0};
        
        REP(i, 4){
            REP(j, 4){
                cin >> ch;
                game[i][j] = 0;
                if(ch == '.'){ game[i][j] = 0; emptySlotFlag = 1; }
                if(ch == 'X'){ game[i][j] = 1; }
                if(ch == 'O'){ game[i][j] = 5; }
                if(ch == 'T'){ game[i][j] = 100; }

                colSum[j] += game[i][j];
                rowSum[i] += game[i][j];
            }
        }

        //REP(i, 4){
          //REP(j,4){
            //cout<< game[i][j] << " ";
          //}
          //cout << endl;
        //}
        
        diaSum[0] = game[0][0] + game[1][1] + game[2][2] + game[3][3];
        diaSum[1] = game[0][3] + game[1][2] + game[2][1] + game[3][0];
        
        REP(i, 4){
            if( colSum[i] == 4 || colSum[i] == 103 ){
                xWon = 1;
                break;
            }
            if( colSum[i] == 20 || colSum[i] == 115 ){
                oWon = 1;
                break;
            }
            if( rowSum[i] == 4 || rowSum[i] == 103 ){
                xWon = 1;
                break;
            }
            if( rowSum[i] == 20 || rowSum[i] == 115 ){
                oWon = 1;
                break;
            }
        }
        REP(i, 2){
            if( diaSum[i] == 4 || diaSum[i] == 103 ){
                xWon = 1;
                break;
            }
            if( diaSum[i] == 20 || diaSum[i] == 115 ){
                oWon = 1;
                break;
            }
        }
        
        if( xWon == 1) printf("Case #%d: X won\n", ti+1);
        else if( oWon == 1) printf("Case #%d: O won\n", ti+1);
        else if( emptySlotFlag == 1) printf("Case #%d: Game has not completed\n", ti+1);
        else printf("Case #%d: Draw\n", ti+1);
        

    }
    return 0;
}
