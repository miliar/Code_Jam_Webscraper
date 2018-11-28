
#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
#include <cassert>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())

int dp[2000000];

int N;
int A[100], B[100], V[100];

bool doit(int n, int msk, bool output=false) {
	int& ret=dp[msk];
	if(ret) return ret>0;
	if(msk+1==(1<<N)) return true;
	fu(i,0,N) if(!(msk&1<<i)) {
		int aa=1, bb=1;
		fu(j,0,i) if(msk&(1<<j)) aa=max(aa, 1+A[j]);
		fu(j,i+1,N) if(msk&(1<<j)) bb=max(bb, 1+B[j]);
		if(aa!=A[i] || bb!=B[i]) continue;
		if(doit(n+1,msk|(1<<i))) {
			ret=i+1;
			return true;
		}
	}
	ret=-1;
	return false;
}

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
	        memset(dp,0,sizeof(dp));
		cout << "Case #" << ts << ":";
		cin >> N;
		fu(i,0,N) cin >> A[i];
		fu(i,0,N) cin >> B[i];
		fu(i,0,N) if(A[i]==1 && B[i]==1) {
			bool ret = doit(2, 1<<i, true);
			assert(ret);
			int cur=i;
			int msk=0;
			for(int n=1; n<=N; n++) {
				//cout << cur << endl;
				V[cur]=n;
				msk |= 1<<cur;
				cur = dp[msk]-1;
			}
			break;
		}
		fu(i,0,N) cout << " " << V[i]; cout << endl;
        }
}
