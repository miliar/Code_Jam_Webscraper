#include <bits/stdc++.h>
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
#define PI 3.14159265358979323846
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;

typedef long double dbl;
#define BITS(a) __builtin_popcount(a)

dbl Eval(const vector<dbl>& t){
  int mid = 500;
  int n = sz(t);

  vector<dbl> cdp(1000), ndp(1000);
  fill(all(cdp), 0.0);
  cdp[mid + 0] = 1.0;

  for(int i = 0;i < n;++i){
    fill(all(ndp), 0.0);
    for(int d = -i;d <= i;++d){
      dbl prev = cdp[mid + d];
      ndp[mid + d + 1] += prev * t[i];
      ndp[mid + d - 1] += prev * (1.0 - t[i]);
    }
    cdp.swap(ndp);
  }

  return cdp[mid + 0];
}

int CASE = 0;
void Doit(){
  ++CASE;
  cerr << "Case: " << CASE << endl;

  int n, k;
  cin >> n >> k;
  vector<dbl> in(n);
  for(int i = 0;i < n;++i) cin >> in[i];

  sort(all(in));
  dbl res = 0;
  auto in_ = in;


  for(int lt = 0;lt <= k;++lt){
    int rt = k - lt;
    n = k;
    in.clear();
    for(int i = 0;i < lt;++i)
      in.pb(in_[i]);
    for(int i = 0;i < rt;++i)
      in.pb(in_[sz(in_) - 1 - i]);

  /*
  for(int m = 0;m < (1 << n);++m){
    if(BITS(m) != k) continue;
    dbl use = 0.0;
    int need = k / 2;
    for(int s = m;;s = (s - 1) & m){
	  if(s == 0)  break;
      if(BITS(s) != need) continue;
      dbl cur = 1.0;
      for(int i = 0;i < n;++i){
        if(m & (1 << i)){
          if(s & (1 << i)) cur *= in[i];
          else cur *= 1.0 - in[i];
        }
      }
      use += cur;
    }
    res = max(res, use);
  }
  */
  auto use = Eval(in);
  res = max(use, res);

  }

  printf("Case #%d: %.12f\n", CASE, (double) res);
}

int main(){
  int Q;
  scanf("%d", &Q);
  while(Q-- > 0) Doit();
  return 0;
}
