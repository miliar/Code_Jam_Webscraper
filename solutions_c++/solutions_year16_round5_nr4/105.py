#include<bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define UPD(a,b) { a = (a + (b)) % MD; }

int n, L;
string g[1111], B;
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		cin >> n >> L;
		For(i,1,n) cin >> g[i];
		cin >> B;
		bool nosol = false ;
		For(i,1,n) if (g[i] == B) {
			nosol = true;
			break ;
		}
		if (nosol) {
			puts("impossible");
			continue ;
		}
		if (L == 1) {
			puts("0? 0");
		} else {
			For(i,1,L - 1) putchar('?');
			putchar(' ');
			string s2 = "10?";
			For(i,1,L) s2 += "01";
			cout << s2 << endl;
		}
	}
	return 0;
}
