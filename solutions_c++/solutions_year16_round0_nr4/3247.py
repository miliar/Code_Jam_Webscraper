//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <bits/stdc++.h>
using namespace std;
#define pb push_back
typedef long long ll;
const int iinf = 0x7fffffff;
const ll linf = ~(1LL<<63);
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef map<ll, int> mli;
typedef map<ll, ll> mll;
template<typename T>
inline T gcd(T a, T b) { 
	if(a < b) return gcd(b, a); 
	if(b == 0) return a; 
	return gcd(b, a%b);
}
template<typename C> // container
inline void sort(C& v) {
	sort(v.begin(), v.end());
}
inline void println(int u) { printf("%d\n", u); }
inline void printsp(int u) { printf("%d ", u); }

// -------------------- Spliters ------------------------
const int maxn = 101;
//不检查ll是猪!!!


int main()
{
	//ios::sync_with_stdio(0);
	int T;
	cin>>T;
	for(int k = 0; k < T; k++) {
		ll K, C, S;
		cin>>K>>C>>S;
		ll dp[101];
		for(int i = 1; i <= K; i++) {
			dp[i] = i;
		}
		for(int i = 1; i < C; i++) {
			for(int j = 1; j <= K; j++) {
				dp[j] = K * (dp[j] - 1) + j;
			}
		}
		// K == S
		cout<<"Case #"<<k+1<<": ";
		for(int i = 1; i <= K; i++) {
			cout<<dp[i]<<" ";
		}
		cout<<endl;
	}

	return 0;
}
//--USE C++11


