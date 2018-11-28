#include <cstdio>
#include <algorithm>
#include <set>
#define mp make_pair
#define pb push_back
#define fir first
#define sec second
using namespace std;
typedef long long ll;

template<typename T> inline void R(T &x) {
	char ch = getchar(); x = 0;
	for (; ch<'0'; ch=getchar());
	for (; ch>='0'; ch=getchar()) x = x*10+ch-'0';
}
const int N = 1005;
int n, s;
multiset<int> S;
void run() {
	R(n); R(s);
	int x;
	S.clear();
	for (int i=1; i<=n; ++i) {
		R(x);
		S.insert(x);
	}
	multiset<int>::iterator it;
	int cnt = 0;
	while (!S.empty()) {
		++cnt;
		x = *S.begin();
		S.erase(S.begin());
		it = S.upper_bound(s - x);
		if (S.begin() != it) {
			--it;
			S.erase(it);
		}
	}
	printf("%d\n", cnt);
}
int main() {
	int T; R(T);
	for (int i=1; i<=T; ++i) {
		printf("Case #%d: ", i);
		run();
	}
	return 0;
}
