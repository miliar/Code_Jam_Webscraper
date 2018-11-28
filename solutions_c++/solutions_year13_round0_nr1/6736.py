#include <algorithm>
#include <iostream>
#include <sstream>
#include <string.h>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#include <cctype>
#include <list>

#define INF 2000000000
#define ll long long
#define PI 3.1415926535897932384626433832795
#define all(a) a.begin(), a.end()
#define F first
#define S second
#define pb push_back
#define mp make_pair
#define y1 olololo1
#define y0 olololo2
#define m0(a) memset(a,0,sizeof(a))

using namespace std;
const long long LLINF = 9223372036854775806;


char a[100][100];

int t;

void solve(){
    int n = 4, emp = 0;
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= n; ++j){
            cin >> a[i][j];
            if (a[i][j] == '.')++emp;
        }
    // Check ----> && down;
    for (int i = 1; i <= n; ++i){
        int x=0,o=0, xx=0,oo=0;;
        for (int j = 1; j <= n; ++j){
            if (a[i][j] =='X') ++x;
            else if (a[i][j] == 'O')++o;
            else if (a[i][j] == 'T')++x,++o;
            if (a[j][i] =='X') ++xx;
            else if (a[j][i] == 'O')++oo;
            else if (a[j][i] == 'T')++xx,++oo;
        }
        if ((x==4&&o<=1)||(xx==4&&oo<=1)){
            cout << "X won";
            return;
        }
        if ((o==4&&x<=1)||(oo==4&&xx<=1)){
            cout << "O won";
            return;
        }
    }
    //CHeck diag
    int i=1,j=1,x=0,o=0;
    for(int it=1; it<=4; ++it,++i,++j){
        if (a[i][j] =='X') ++x;
        else if (a[i][j] == 'O')++o;
        else if (a[i][j] == 'T')++x,++o;
    }
    if ((x==4&&o<=1)){
        cout << "X won";
        return;
    }
    if ((o==4&&x<=1)){
        cout << "O won";
        return;
    }
    i=1,j=n;
    x=0,o=0;
    for (int it=1; it<=4; ++it,++i,--j){
        if (a[i][j] =='X') ++x;
        else if (a[i][j] == 'O')++o;
        else if (a[i][j] == 'T')++x,++o;
    }
    if ((x==4&&o<=1)){
        cout << "X won";
        return;
    }
    if ((o==4&&x<=1)){
        cout << "O won";
        return;
    }
    if (emp==0) cout << "Draw";
    else cout << "Game has not completed";
}

int main(){
     freopen("A-large.in.txt","r",stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin >> t;
    for (int it = 1; it <= t; ++it){
        cout << "Case #"<<it << ": ";
        solve();
        cout << "\n";
    }
    
    
    return 0;
    
}