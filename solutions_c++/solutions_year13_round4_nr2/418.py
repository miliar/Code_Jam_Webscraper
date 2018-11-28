
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

i64 best_pos(int N, i64 i) {
	if(i+1==(1LL<<N)) return i;
	return best_pos(N-1, (i+1)/2);
}

i64 worst_pos(int N, i64 i) {
	if(i==0) return 0;
	//cout << '!' << N << " " << i << endl;
	//if(i+1==(1LL<<N)) return i;
	i64 A=i;
	i64 B=(1LL<<N)-i-1;
	return (1LL<<N-1) + worst_pos(N-1, max(0LL,A-1)/2);
	//if(A<B) return worst_pos(N-1, i);
	//else return worst_pos(N-1, i-(A-B)/2);
}

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		cout << "Case #" << ts << ": ";
		int N; i64 P;
		cin >> N >> P;
		//cout << " " << guar_win(N,P) << " " << win(N,P) << endl;
		//for(int i=0; i<(1<<N); i++) cout << best_pos(N, i) << " "; cout << endl;
		//for(int i=0; i<(1<<N); i++) cout << worst_pos(N, i) << " "; cout << endl;
		i64 Y=0, Z=0;
		//for(int i=0; i<(1<<N); i++) if(worst_pos(N,i)<P) Y=i;
		//for(int i=0; i<(1<<N); i++) if(best_pos(N,i)<P) Z=i;

		{
			i64 lo=0, hi=1LL<<N;
			while(lo+1<hi) {
				i64 mid=(lo+hi+1)/2;
				if(worst_pos(N,mid)>=P) hi=mid;
				else lo=mid;
			}
			//assert(Y==lo);
			Y=lo;
		}

		{
			i64 lo=0, hi=1LL<<N;
			while(lo+1<hi) {
				i64 mid=(lo+hi+1)/2;
				if(best_pos(N,mid)>=P) hi=mid;
				else lo=mid;
			}
			//assert(Z==lo);
			Z=lo;
		}

		cout << Y << " " << Z << endl;
        }
}
