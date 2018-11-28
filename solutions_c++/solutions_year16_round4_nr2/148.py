#include <cstdio>
#include <vector>
#include <cassert>

using namespace std;

typedef long long ll;
typedef double ld;

vector<vector<ld>> probabilities(vector<ld> A) {
  vector<vector<ld>> B(A.size()+1, vector<ld>(A.size()+1, 0.0));
  B[0][0] = 1.0;
  for(ll i=1; i<B.size(); i++) {
    for(ll v=0; v<=i; v++) {
      B[i][v] = (v>0 ? B[i-1][v-1]*A[i-1] : 0.0) + B[i-1][v]*(1.0-A[i-1]);
      //  printf("B[%lld][%lld] = %f\n", i, v, B[i][v]);
    }
  }
  return B;
}
ld ans(vector<ld> A) {
  vector<vector<ld>> B = probabilities(A);
  return B[A.size()][A.size()/2];
}

bool bit_set(ll set, ll bit) {
  return ((set>>bit)&1)==1;
}
ld slow(ll n, ll k, vector<ld> P) {
  ld best = 0.0;
  for(ll a=0; a<(1<<n); a++) {
    vector<ld> A;
    for(ll i=0; i<n; i++) {
      if(bit_set(a, i)) {
        A.push_back(P[i]);
      }
    }
    if(A.size() == k && ans(A) > best) {
      best = ans(A);
    }
  }
  /*
  bool show = false;
  for(ll a=0; a<(1<<n); a++) {
    vector<ld> A;
    for(ll i=0; i<n; i++) {
      if(bit_set(a, i)) {
        A.push_back(P[i]);
      }
    }
    if(A.size() == k && ans(A) == best && !show) {
      show = true;
      for(ll i=0; i<A.size(); i++) {
        printf("%f%s", A[i], i==A.size()-1?"\n":" ");
      }
    }
  }
  */
  return best;
}

int main() {
  ll T;
  scanf("%lld", &T);
  for(ll cas=1; cas<=T; cas++) {
    ll n, k;
    scanf("%lld %lld", &n, &k);
    vector<ld> P(n, 0.0);
    for(ll i=0; i<n; i++) {
      scanf("%lf", &P[i]);
    }
    sort(P.begin(), P.end());
    /*
    for(ll i=0; i<P.size(); i++) {
      printf("%f%s", P[i], i==P.size()-1?"\n":" ");
    }
    */

    ld best = 0.0;
    for(ll p=0; p<=k; p++) {
      vector<ld> A;
      for(ll i=0; i<p; i++) {
        A.push_back(P[i]);
      }
      for(ll i=0; i<(k-p); i++) {
        A.push_back(P[P.size()-1-i]);
      }
      best = max(best, ans(A));
    }

    /*
       vector<vector<ld>> HI(k+1, vector<ld>(k+1, 0.0));

       HI[0][0] = {1.0, 0.0};

       for(ll i=0; i<n; i++) {
       for(ll c=k; c>=0; c--) {
       for(ll v=0; v<=c; v++) {
       HI[c][v] = max(HI[c][v], (c>0 && v>0 ? HI[c-1][v-1]*P[i] : 0.0) + (c>0 ? HI[c-1][v]*(1.0-P[i]) : 0.0));
       }
       }
       }

*/
    //printf("Case #%lld: %.9f\n", cas, slow(n, k, P));
    printf("Case #%lld: %.9f\n", cas, best);
  }
}
