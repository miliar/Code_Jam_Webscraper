#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
typedef long long Long;
typedef pair<Long,Long> PII;

//int mem[1024][1024];
//int dp(int N, int L){
//	if(N <= L)return 0;
//	if(mem[N][L] != -1)return mem[N][L];
//	return mem[N][L] = dp(N/2, L) + dp((N+1)/2, L) + 1;
//}
//int mem2[1024][1024];
//int ma(int N, int L){
//	if(N <= L)return N;
//	if(mem2[N][L] != -1)return mem2[N][L];
//	return mem2[N][L] = max(ma(N/2, L) , ma((N+1)/2, L));
//}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
//	memset(mem,-1,sizeof(mem));
//	memset(mem2,-1,sizeof(mem2));
//	cout << dp(998,6) << endl;
//	cout << ma(998,6) << endl;
//	return 0;
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC ; ++tc){
		int D;
		cin >> D;
		vector<int> V(D);
		for (int i = 0; i < D; ++i) {
			cin >> V[i];
		}
		int mi = 1000000;
		for(int i = 1; i <= 1000; ++i){
			int sp = 0, m = 0;
			for(int j = 0; j < D; ++j){
//				sp += dp(V[j], i);
				int pcs = (V[j]+(i-1))/i;
				sp += pcs - 1;
//				m = max(ma(V[j],i), m);
				m = max(m , (V[j]+(pcs-1))/pcs);
			}
			mi = min(m + sp, mi);
//			cout << i << " " << m << " " << sp << endl;
		}
		cout << "Case #" << tc << ": " << mi << endl;
	}	
}
