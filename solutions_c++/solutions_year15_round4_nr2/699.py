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
double R[Nmax], C[Nmax];
const double eps = 1e-11;
double V,X;

double f(double V1) {
       return max(V1 / R[1], (V - V1) / R[2]);
}
int main() {
    ios_base::sync_with_stdio(0);
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;
    cin >> T;
    while (T --> 0) {
          int n;
          cin >> n >> V >> X;
          
          cout.precision(10);
          for (int i = 1;i <= n; i ++)
              cin >> R[i] >> C[i];
          
           Case();
          if (n > 2) continue;
          if (n == 1) {
             if (X != C[1]) {
                   cout << "IMPOSSIBLE\n";
             }
             else
                 cout << fixed << (V * 1.0 / R[1]) << endl;
             continue;
          }
          
          if (X < min(C[1], C[2]) || X > max(C[1], C[2])) {
                cout << "IMPOSSIBLE\n";
                continue;
          }
          if (C[1] != C[2]) {
             double V2 = (X * V - V * C[1]) / (C[2] - C[1]);
             assert(V2 > -eps);
             cout << fixed << max((V - V2) / R[1], V2 / R[2]) << endl;
          }
          else
          {
              double Vl = 0, Vr = V;
              while (abs(Vr - Vl) > eps) {
                    double mid = (Vr - Vl) / 3.0;
                    if (f(Vl + mid) + eps < f(Vr - mid)) 
                       Vr -= mid;
                    else
                        Vl += mid;
              }    
              cout << fixed << f(Vl) << endl;
          } 
    }
    //pause;
    return 0;
}
