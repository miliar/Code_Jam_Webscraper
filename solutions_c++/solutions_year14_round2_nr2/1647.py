#include <bits/stdc++.h>

using namespace std;
#define CLR(a) memset(a, 0, sizeof(a))
#define ABS(X) ( (X) > 0 ? (X) : ( -(X) ) )
#define SZ(V) (int )V.size()
#define ALL(V) V.begin(), V.end()
#define RALL(V) V.rbegin(), V.rend()
#define FORN(i, n) for(LL i = 0; i < n; i++)
#define FORAB(i, a, b) for(LL i = a; i <= b; i++)
#define pll pair < long long int, long long int >
#define pii pair < int, int >
#define psi pair < string, int >
#define PB push_back  
#define MP make_pair
#define F first
#define S second
#define MOD 1000000007LL

typedef pair<int,int> PII;
typedef pair<double, double> PDD;
typedef long long LL;

int main(){
	LL test,t;
	cin >> t;
	FORN(test,t){
		LL A,B,K,ans=0;
		cin >> A >> B >> K;
		FORN(i,A){
			FORN(j,B){
				if((i&j)<K){
					ans++;
				}
			}
		}
		cout << "Case #" << test+1 << ": " << ans << endl;
	}
	return 0;
}