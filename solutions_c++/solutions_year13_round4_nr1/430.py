
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())
const i64 MOD=1000002013;

i64 cost(i64 N, i64 d) {
	return ((N+1)*d - d*(d+1)/2)%MOD;
}

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ": ";
		int N,M;
		cin >> N >> M;
		vector<int> O(M),E(M),P(M);
		fu(i,0,M) cin >> O[i] >> E[i] >> P[i];
		i64 base=0;
		fu(i,0,M) base = (base + P[i]*cost(N,E[i]-O[i]))%MOD;
		vector<int> po(N+1), eo(N+1);
		fu(m,0,M) po[O[m]]+=P[m];
		fu(m,0,M) eo[E[m]]+=P[m];
		i64 act=0;
		priority_queue<int> cur;
		fu(n,0,N+1) {
			fu(i,0,po[n]) cur.push(n);
			fu(i,0,eo[n]) {
				int j=cur.top();
				cur.pop();
				act += cost(N,n-j);
				act %= MOD;
			}
		}
		cout << (base-act)%MOD << endl;
        }
}
