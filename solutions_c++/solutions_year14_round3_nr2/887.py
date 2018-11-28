#include <iostream>
#include <algorithm>

using namespace std;

int solve() {
	int N;
	cin >> N;
	
	pair<string,int> strs[N];
	for (int i = 0; i < N; i++) {
		cin >> strs[i].first;
		strs[i].second = i;
	}
		
	sort(strs, strs+N);
	int res = 0;
	
	do {
		int used[26] = {0};
		int ok = 1;
		for (int i = 0; i < N && ok; i++) {
			for (int j = 0; j < (int)strs[i].first.size() && ok; j++) {
				if (j > 0 && strs[i].first[j] != strs[i].first[j-1] && used[strs[i].first[j]-'a']) {
					ok = 0;
					/*cout << "NO: ";
					for (int i = 0; i < N; i++)
						cout << strs[i].first;
					cout << endl;*/
				}
				if (i > 0 && j == 0 && strs[i].first[0] != strs[i-1].first[strs[i-1].first.size()-1] && used[strs[i].first[j]-'a']) {
					ok = 0;
					/*cout << "NO2: ";
					for (int i = 0; i < N; i++)
						cout << strs[i].first;
					cout << endl;*/
					
				}
				used[strs[i].first[j]-'a'] = 1;
			}			
		}
		if (ok) {
			 res++;
			 /*for (int i = 0; i < N; i++)
				cout << strs[i].first;
			cout << endl;*/
		 }
	} while (next_permutation(strs, strs+N));
	return res;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) 
		cout << "Case #" << t << ": " << solve() << endl;
}
