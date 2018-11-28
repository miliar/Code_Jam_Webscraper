#include<iostream>
#include<cstdio>
#include<stack>
#include<queue>
#include<set>
#include<iomanip>
#include<complex>
#include<vector>
#include<map>
#include<algorithm>
#include<cmath>
#include<string>
#include<bitset>
#include<memory.h>
#include<cassert>
#include<ctime>

using namespace std;

#pragma comment(linker, "/STACK:36777216")

#define For(i,l,r) for (int i = l; i < r + 1; i ++)
#define ForI(it , s , T) for (T :: iterator it = s.begin(); it != s.end() ; ++ it )
#define LL long long
#define iinf 2000000000
#define linf 4000000000000000000LL
#define MOD  (1000000007)
#define Pi 3.1415926535897932384
#define bit(mask,i) ((mask>>i)&1)
#define pb(x) push_back(x)
#define mk(x,y) make_pair(x,y)
#define sqr(x) ((x)*(x))
#define pause cin.get();cin.get();
#define fir first
#define sec second
#define ln(x) log(x)
#define pii pair<int,int>
#define y1 y23423423

const int Nmax = 600100;
const int Direction[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

inline void Case() {
       static int numb = 0;
       numb ++;
       cout << "Case #" << numb << ": ";
}
int n,m;
char ch[500][500];

bool IN(int x,int y) {
     if (x < 1 || x > n) return 0;
     if (y < 1 || y > m) return 0;
     return 1;
}
int to(char c) {
    if (c == '>') return 1;
    if (c == '<') return 3;
    if (c == 'v') return 2;
    if (c == '^') return 0;
}
int main() {
    ios_base::sync_with_stdio(0);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin >> T;
    while (T --> 0) {
          cin >> n >> m;
          for (int i = 1;i <= n; i ++)
              for (int j = 1; j <= m ;j ++) {
                  cin >> ch[i][j];
              }
          
          Case();
          int answer = 0;
          bool ok = true;
          for (int i = 1;i <= n ;i ++) {
              if (ok)
              for (int j = 1;j <= m ;j ++) {
                  if (ch[i][j] == '.') continue;
                  
                  int t = to(ch[i][j]);
                  
                  int cc[5] = {0};
                  for (int q = 0; q < 4; q ++ ){
                      int x = i, y = j;
                      while (IN(x,y)) {
                            if (ch[x][y] != '.') cc[q]++;
                            x += Direction[q][0];
                            y += Direction[q][1];
                      }
                  }
                  
                  if (cc[0] == 1 && cc[1] == 1 && cc[2] == 1 && cc[3] == 1) {
                           cout << "IMPOSSIBLE\n";
                           ok = false;
                           break;
                  }
                  
                  if (cc[t] > 1) continue;
                  answer ++;
                  
              }
          }
          
          if (!ok) continue;
          cout << answer << endl;
    }
    //pause;
    return 0;
}
