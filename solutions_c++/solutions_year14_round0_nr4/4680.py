#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<ctime>
#include<cmath>

#include<algorithm>
#include<bitset>
#include<complex>
#include<deque>
#include<iostream>
#include<map>
#include<numeric>
#include<queue>
#include<stack>
#include<string>
#include<set>
#include<vector>
using namespace std;

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define sz(a) (int((a).size()))
#define all(a) (a).begin(), (a).end()

#define For(it,c) for(typeof(c) it = ((c).begin()); it != ((c).end()) ; ++it)

#define forn(i,n) for (int i=0; i<int(n); ++i)
#define fornd(i,n) for (int i=int(n)-1; i>=0; --i)
#define forab(i,a,b) for (int i=int(a); i<int(b); ++i)

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

typedef complex<int> cI;
typedef complex<double> cD;

typedef pair<int,int> pI;
typedef pair<ll, ll> pL;

int n;
vector<double> arrA, arrB;

int ans2(){
  int cnt = 0;
  int L = 0, R = n-1;
  for(int i=n-1;i>=0;i--){
    if(arrA[i] > arrB[R]){
      cnt++;
      L++;
    }else {
      R--;
    }
  }
  return cnt;
}
int ans1(){

  int cnt = 0;
  int L=0;
  for(int i=0;i<n;i++){
    if(arrA[i] > arrB[L]){
      cnt++;
      L++;
    }
  }
  return cnt;
}

int main()
{
  int T;
  double val;

  cin >> T;
  for(int z=1; z<=T; z++){
    cin >> n;
    arrA.clear();
    for(int i=0;i<n;i++){
      cin >> val;
      arrA.pb(val);
    }
    arrB.clear();
    for(int i=0;i<n;i++){
      cin >> val;
      arrB.pb(val);
    }
    sort(all(arrA));
    sort(all(arrB));
    for(int i=0;i<n;i++){
      //printf("%lf ", arrA[i]);
    }
    //puts("");
    for(int i=0;i<n;i++){
      //printf("%lf ", arrB[i]);
    }
    //puts("");
    printf("Case #%d: %d %d\n", z, ans1(), ans2());
  }
  return 0;
}
