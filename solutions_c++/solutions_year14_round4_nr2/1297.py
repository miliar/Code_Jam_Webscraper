#include "../myutil.hpp"

const int64 maxn=1001;

int64 n, a[maxn], b[maxn], c[maxn];

int64 getR(int64 *c, int64 m) {
  int64 r=0;
  for(int64 i=0;i<m;i++) for(int64 j=i+1;j<m;j++) 
    if(c[i]>c[j]) r++;

  return r;
}

template <class T>
bool valid(T first, T last) {
  T maxi = max_element(first, last);
  reverse(maxi+1, last);
  return is_sorted(first, maxi) && is_sorted(maxi+1,last);
}

bool valid(int64 * perm, int n) {
  int tmp[n];
  for (int i=0;i <n;i++) {
    tmp[i] = a[perm[i]];
  }

  return valid(tmp, tmp+n);
}

int64 solve() {
  cin >> n;
  int64 perm[n];
  for (int64 i=0;i<n; i++) {
    cin >> a[i];
    perm[i] = i;
  }

  int64 minCt = 5 * n * n;
  do {
    if (valid(perm, n)) {
      int64 ct = getR(perm, n);
      checkmin(minCt, ct); 
    }
  } while(next_permutation(perm, perm+n));

  return minCt;
}

int main()
{
	int T;
  cin >> T;
	for (int t=1; t<=T; ++t) {
    cout << "Case #" << t << ": " << solve() <<endl;
	}

	return 0;
}
