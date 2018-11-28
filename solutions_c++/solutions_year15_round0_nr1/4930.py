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
int main() {
    ios_base::sync_with_stdio(0);
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    cin >> T;
    while (T --> 0) {
          int n;
          cin >> n;
          string s;
          cin >> s;
          int answer = 0;
          int sum = 0;
          for (int i = 0 ;i <= n ;i ++){
              int k = (s[i] - '0');
              if (sum < i) {
                 answer += (i - sum);
                 sum += (i - sum);
              } 
              sum += k;
          }
          printTest();
          cout << answer << endl;
    }
    //pause;
    return 0;
}
