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
 
#define For(i,l,r) for (int i = l ;i < (int)(r + 1) ; ++ i )
#define ForI(it , s , T) for (T :: iterator it = s.begin(); it != s.end() ; ++ it )
#define LL long long
#define iinf 2000000000
#define linf 4000000000000000000LL
#define MOD  1000000007
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
#define count countBLA
 
const int Direction[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
const int Nmax = 100100;

inline void printTest() {
       static int test_number = 0;
       cout << "Case #";
       test_number ++;
       cout << test_number << ": ";
}
int a[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int f(char c) {
    if (c == 'i') return 2;
    if (c == '1') return 1;
    if (c == 'j') return 3;
    if (c == 'k') return 4;
}
inline void ex(int x) {
       if (x == 0)
          cout << "NO\n";
       else
           cout << "YES\n";
}
int main() {
    ios_base::sync_with_stdio(0);
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T;
    cin >> T;
    while (T --> 0) {
          int l,x;
          cin >> l >> x;
          string s;
          cin >> s;
          string t = s;
          for (int i = 1; i <= x - 1;i ++)
              s += t;
          int result = 1;
          int i = 0;
          printTest();
          while (i < s.size() && result != 2) {
                int sign = (result < 0)?(-1):1;
                result = a[abs(result)][f(s[i])];
                result *= sign;
                i ++;
          }
          if (result != 2)  { ex(0); continue; }
          result = 1;
          while (i < s.size() && result != 3) {
                int sign = (result < 0)?(-1):1;
                result = a[abs(result)][f(s[i])];
                result *= sign;
                i ++;      
          }
          if (result != 3) { ex(0);continue; }
          result = 1;
          while (i < s.size() && result != 4) {
                int sign = (result < 0)?(-1):1;
                result = a[abs(result)][f(s[i])];
                result *= sign;
                i ++;      
          }
          if (result != 4) { ex(0);continue; }
          result = 1;
          while (i < s.size()) {
                int sign = (result < 0)?(-1):1;
                result = a[abs(result)][f(s[i])];
                result *= sign;
                i ++;
          }
          if (result != 1) {ex(0); continue; }
          ex(1);
    }
    //pause;
    return 0;
}
