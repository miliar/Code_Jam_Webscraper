#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>

#define rep(i,n) for(int i=0; i<(n); i++)
#define reps(i,x,n) for(int i=x; i<(n); i++)
#define rrep(i,n) for(int i=(n)-1; i>=0; i--)
#define all(X) (X).begin(),(X).end()
#define X first
#define Y second
#define pb push_back
#define eb emplace_back

using namespace std;
typedef long long int ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

template<class T> bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T> bool chmin(T &a, const T &b) { if (a>b) { a=b; return 1; } return 0; }

template<class A, size_t N, class T> void Fill(A (&a)[N], const T &v){ fill( (T*)a, (T*)(a+N), v ); }

const ll INF = 0x3fffffff;


int main(){
	//ios_base::sync_with_stdio(0);
	int T, K;
	string S;

	cin >> T;
	for(int kase=1; kase<=T; kase++){
		cin >> S >> K;

		int ans = 0;
		rep(i, S.length()){
			if( i <= S.length()-K ){
				if( S[i] == '-' ){
					rep(j,K) S[i+j] = ( S[i+j] == '+' ? '-' : '+' );
					ans++;
				}
			}else{
				if( S[i] == '-' ) ans = -1;
			}
		}

		cout << "Case #" << kase << ": ";
		if( ans < 0 ){
			cout << "IMPOSSIBLE" << endl;
		}else{
			cout << ans << endl;
		}
	}

	return 0;
}
