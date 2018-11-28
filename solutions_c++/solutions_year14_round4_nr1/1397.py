#include "../myutil.hpp"

const int maxn=10001;

int n,x;
int s[maxn];


int solve() {
  cin >> n;
  cin >> x;
  for (int i=0; i<n;i++) {
    cin >> s[i];
  }

  sort(s, s+n);
  
  int ct = 0;
  int l=0, r=n-1;
  while(l<r) {
    if (s[l]+s[r] <= x) {
      ++ct;
      ++l;
      --r;
    } else {
      ++ct;
      --r;
    }
  }
  
  if (l==r) ++ct;

  return ct;
}

int main()
{
//	freopen("A.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int T;
  cin >> T;
	for (int t=1; t<=T; ++t) {
		cout << "Case #" << t << ": " << solve() << endl;
	}

	return 0;
}
