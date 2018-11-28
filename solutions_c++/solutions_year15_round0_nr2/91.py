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
int D , P[1010];
void doit(int CASE = 1){
  scanf("%d" , &D);
  for(int i=0;i<D;++i) scanf("%d" , &P[i]);
  int ANS = *max_element(P , P + D);
  int UP = ANS;
  for(int i=1;i<=UP;++i){
   int sum = i;
   for(int j=0;j<D;++j)
    if(P[j] > i)
     sum += ((P[j] - i) + i - 1) / i;
   relaxMin(ANS , sum);
                        }
  printf("Case #%d: %d\n" , CASE , ANS);
}
int main(){
  int Q; scanf("%d" , &Q);
  for(int i=1;i<=Q;++i) doit(i);
  return 0;
}
