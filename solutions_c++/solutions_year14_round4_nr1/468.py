#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
int N , M , F[10000] ;
void Solve() {
	int ret = 0;
	for ( int i = N ; i >= 1 ; i -- ) if ( F[i] > 0 ) {
		int t ;
		for ( t = i - 1 ; t >= 1 ; t -- ) if ( F[t] > 0 && F[i] + F[t] <= M ) break ;
		ret ++ , F[t] = -1 ;
	}
	cout << ret << "\n" ;
}
int main() {
    freopen("A.in","r",stdin) ; freopen("A.out","w",stdout) ;
	int Test ; cin >> Test ;
	for ( int _ = 1 ; _ <= Test ; _ ++ ) {
        cin >> N >> M ; for (int i = 1; i <= N; ++i) cin >> F[i] ; sort(F + 1, F + N + 1);
		cout << "Case #" << _ << ": " ;
		Solve();
	}
}
