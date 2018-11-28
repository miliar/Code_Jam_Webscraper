#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <list>
#include <set>
#include <climits>
#include <map>
#include <stack>
#include <queue>
#include <complex>
#include <cmath>
#include <sstream>
#include <deque>
#include <utility>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>
using namespace std;
using namespace __gnu_cxx;
#define F first
#define S second
#define mp make_pair
#define oo 1e9
#define FOR(i,n) for (int i = 0 ; i < n ; i++)
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
vector <string> V ;

bool win (char C) {
bool tst  ;
FOR(i,4){
   tst = 1 ;
   FOR(j,4){
       if (V[i][j] != C && V[i][j] != 'T')tst = 0 ;
      }
    if (tst)return 1 ;
   }

FOR(i,4){
   tst = 1 ;
   FOR(j,4){
       if (V[j][i] != C && V[i][j] != 'T')tst = 0 ;
      }
    if (tst)return 1 ;
   }
tst = 1 ;
FOR(i,4)if (V[i][i] != C && V[i][i] != 'T')tst = 0 ;
if(tst)return 1  ;
tst = 1 ;
for (int i = 0 , k = 3 ; i < 4 ; i++ , k--){
    if (V[i][k] != C && V[i][k] != 'T')tst = 0 ;
}
if (tst)return 1 ;
return 0 ;
}

bool not_compelted (){
FOR(i,4)
   FOR(j,4)
       if (V[i][j] == '.')return true ;
return false ;
}


int main () {
READ("input_codejame.txt");
WRITE("output_codejame.txt");
int T  , n , nt = 0 , I , J;
char c ;
string s ;
cin>>T;
while(T--){
    n = 4 ;
    V.clear() ;
    while(n--){
        cin>>s ;
        V.push_back(s) ;
    }
if (win('O'))cout<<"Case #"<<++nt<<": O won"<<endl;
else if (win('X'))cout<<"Case #"<<++nt<<": X won"<<endl;
else if (not_compelted())cout<<"Case #"<<++nt<<": Game has not completed"<<endl;
else cout<<"Case #"<<++nt<<": Draw"<<endl;
}



}
