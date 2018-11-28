#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#define REP(i, a, b)		for(i = (int)a; i<=(int)b ; i++)
#define FOR(i, N)			REP(i, 0, N-1)

#define VL					vector<long long>

using namespace std;

int main(){
	ifstream cin("D.in");
	ofstream cout("D-Large.out");

	int t, T;
	cin >> T;
	REP(t, 1, T) {
		int i;
		long long K, C, S;
		cin >> K >> C >> S;

		int req = (K + C - 1) / C;
		if (S < req){
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			continue;
		}

		VL V(K);
		FOR(i, K) V[i] = i;

		VL ans;
		int student;
		FOR(student, req){
			int studentStartIndex = student*C;
			long long val = 0;
			long long pwr = 1;
			FOR(i, C){
				if (studentStartIndex + i >= K) break;
				int cur = studentStartIndex + i;
				val += V[cur] * pwr;
				pwr *= K;
			}
			ans.push_back(val);
		}

		cout << "Case #" << t << ":";
		FOR(i, req) cout << " " << ans[i]+1;
		cout << endl;
	}
	return 0;
}