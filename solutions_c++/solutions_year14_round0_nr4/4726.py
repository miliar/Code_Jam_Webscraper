#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define REP(I,N) for(int I=0;I<(N);I++)

int main(){
	int T;
	cin >> T;

	REP(i,T){
		int N;
		cin >> N;

		double A[1001],B[1001];

		REP(j,N) cin >> A[j];
		REP(j,N) cin >> B[j];

		sort(A,A+N);
		sort(B,B+N);

		vector<double> a,b;

		int res = 0;
		
		REP(j,N){
			a.clear();
			b.clear();
			FOR(k,j,N-1) a.push_back(A[k]);
			FOR(k,0,N-j-1) b.push_back(B[k]);

			bool ok = true;
			REP(k,a.size())
				if(a[k]<b[k]) ok = false;

			if(ok){
				res = N-j;
				break;
			}
		}
		
		cout << "Case #" << i+1 << ": " << res << " ";

		res = 0;
		REP(j,N){
			double best = 2.0;
			int idx = 0;
			REP(k,N)
				if(B[k]>A[j]&&B[k]<best){
					best = B[k];
					idx = k;
				}
			if(best<2.0) B[idx] = -1;
			else
				++res;
		}

		cout << res << endl;
	}	

	return 0;
}
