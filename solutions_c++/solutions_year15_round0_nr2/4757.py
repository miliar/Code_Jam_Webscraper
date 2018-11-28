#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		int D;
		vector<int> P;
		cin >> D;

		int global_max = -1;
		for (int i = 0; i < D; i++){
			int p;
			cin >> p;
			global_max = max(global_max, p);
			P.push_back(p);
		}

		int best = global_max;
		for (int i = 1; i <= global_max; ++i){
			int s = 0;
			for (int j = 0; j < D; j++){
				int n = P[j];
				s += (n - 1)/i;
			}
			best = min(best, i + s);
		}

		cout << "Case #" << t << ": " << best << endl;
	}
}
