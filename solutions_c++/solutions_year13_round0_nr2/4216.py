#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iomanip>
#include <cmath>
#include <string>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <iostream>
#include <sstream>
#include <cctype>
#include <ctime>
#include <float.h>
#include <bitset>
#include <set>
#include <utility>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

#define swap(a,b) {a^=b;b^a=;a^=b;}
#define For(i,a,b) for (int i(a),_b(b); i <= _b ; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b ; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n ; ++i)
#define Repd(i,n) for (int i((n)-1); i>=0 ; --i)
inline int min(int a,int b){return a<b?a:b;}
inline int max(int a,int b){return a>b?a:b;}

int board[101][101];
int T, N, M;

bool checkRow(int x, int y){
    Rep(i,M) if (board[x][i] > board[x][y]) return true;
    return false;
}

bool checkCol(int x, int y){
    Rep(i,N) if (board[i][y] > board[x][y]) return true;
    return false;
}

string check(){
    Rep(i, N)
        Rep(j, M)
            if (checkRow(i,j) && checkCol(i,j)) return "NO";
    return "YES";
}

int main(){
    freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
    cin >> T;
    Rep(i, T){
        printf("Case #%d: ", i+1);
        cin >> N >> M;
        Rep(j, N) Rep (k, M) cin >> board[j][k];
        cout << check() << endl;
    }
    return 0;
}