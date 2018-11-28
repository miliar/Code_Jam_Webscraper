#include <bits/stdc++.h>

using namespace std;

int main() {
	int T, final;
	cin >> T;
	final = T;
	while(T>0) {
		T--;
		int C, D, V;
		cin >> C >> D >> V;

		std::map<int, bool> sumPres;
		set<int> sums;
		sums.insert(0);

		for (int i = 0; i < D; ++i)
		{
			int temp;
			cin >> temp;
			set<int> oldSums = sums;
			for(auto it=oldSums.begin(); it!=oldSums.end(); it++) {
				if(!sumPres[temp + (*it)]) {
					sums.insert(temp + (*it));
					sumPres[temp + (*it)] = true;
				}
			}
		}
		int ans = 0;

		for (int i = 1; i <= V; ++i)
		{
			if(!sumPres[i]) {
				ans++;
				int temp = i;
				set<int> oldSums = sums;
				for(auto it=oldSums.begin(); it!=oldSums.end(); it++) {
					if(!sumPres[temp + (*it)]) {
						sums.insert(temp + (*it));
						sumPres[temp + (*it)] = true;
					}
				}
			}
		}

		cout << "Case #" << final-T << ": " << ans << endl;
	}


}