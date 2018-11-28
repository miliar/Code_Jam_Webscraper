#include "cstdio"
#include "iostream"
#include "vector"
#include "algorithm"
#include "cstring"
#include "set"
#include "map"
#define runtime() ((double)clock() / CLOCKS_PER_SEC)
#define rep(i, n) for(int i=0; i<n; i++)
#define repp(i, a, b) for(int i=a; i<a+b; i++)
using namespace std;
inline int getint(){
  char c = getchar();
  for(;c<'0'||c>'9';) c = getchar();
  int x = 0;
  for(;c>='0' && c<='9'; c = getchar()) x*=10, x+=c-'0';
  return x;
}
const int maxn = 20000;
int x[maxn];
int n,m;
multiset<int> s;
multiset<int>::iterator it;
int main(int argc, char const *argv[])
{
	int cass;cin>>cass;
	repp(cas, 1, cass){
		s.clear();
		n = getint(), m = getint();
		int ans = 0;
		rep(i, n)	x[i] = getint();
		sort(x, x+n);
		for(int i = n-1; i>=0; i--){
			it = s.lower_bound(x[i]);
			if(it==s.end()){
				ans++;
				s.insert(m - x[i]);
			}else{
				int r = *it - x[i];
				s.erase(it);
			}
		}
		printf("Case #%d: %d\n", cas, ans);
	}	
	return 0;
}