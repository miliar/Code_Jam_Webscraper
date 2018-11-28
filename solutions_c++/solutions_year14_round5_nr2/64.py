#ifdef _WIN32
#  define LL "%I64d"
#else
#  define LL "%Ld"
#endif

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <algorithm>
#include <complex>
#include <utility>
#include <cassert>
using namespace std;
#define null NULL
#define mp make_pair
#define pb(a) push_back(a)
#define sz(a) ((int)(a).size())
#define all(a) a.begin() , a.end()
#define fi first
#define se second
#define relaxMin(a , b) (a) = min((a),(b))
#define relaxMax(a , b) (a) = max((a),(b))
#define SQR(a) ((a)*(a))
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;
int dp[200][2000];
void doit(int CASE = 1){
  int D , T , N;
  scanf("%d%d%d" , &D , &T , &N);
  vi H(N) , G(N);
  for(int i=0;i<N;++i)
   scanf("%d%d" , &H[i] , &G[i]);
  int MB = 10 * N + 5;
  for(int i=0;i<=N;++i)
   for(int j=0;j<MB;++j)
    dp[i][j] = -1;
  dp[0][1] = 0;
  for(int i=0;i<N;++i){
   int ni = i+1;
   for(int j=0;j<MB;++j){
    if(dp[i][j] == -1) continue;
    int cavb = j;
    int cs = dp[i][j];
    // TAKE
    int cs1 = cs;
    int rem = H[i] % T;
    int avb1 = cavb + H[i] / T;
    if(rem == 0) rem = T , --avb1;
    int need = (rem + D - 1) / D;
    if(need <= avb1){
     avb1 -= need , cs1 += G[i];
     if(dp[ni][avb1] == -1) dp[ni][avb1] = cs1;
     relaxMax(dp[ni][avb1] , cs1);
                    }
    // NOT TAKE
    int avb2 = cavb + (H[i] + T - 1) / T;
    if(dp[ni][avb2] == -1) dp[ni][avb2] = cs;
    relaxMax(dp[ni][avb2] , cs);
                        }
                      }
  int BEST = 0;
  for(int j=0;j<MB;++j)
   relaxMax(BEST , dp[N][j]);
  printf("Case #%d: %d\n" , CASE , BEST);
}
int main(){
  int Q;
  scanf("%d" , &Q);
  for(int i=0;i<Q;++i)
   doit(i+1);
  return 0;
}
