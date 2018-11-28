#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int n, d;
int p[1010];

int idxmax() {
	int idx_max = 0;
	for (int i = 0; i < d; i++) {
		if (p[idx_max] < p[i])
			idx_max = i;
	}
	return idx_max;
}


int solve() {
	int idx = idxmax();
	int ans = -1;
	for (int i = 1; i <= p[idx]; i++) {
		int curr_ans = 0;
		for (int j = 0; j < d; j++) {
			curr_ans += p[j] / i + (p[j] % i == 0 ? 0 : 1);
			curr_ans--;
		}
		
		if (ans == -1 || ans > curr_ans + i)
			ans = curr_ans + i;
	}
	return ans;
}


int main(){
	cin >> n;
	for (int i = 0; i< n; i++){
		cin >> d;
		for (int j = 0; j < d; j++) {
			cin >> p[j];
		}
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}
	return 0;
}
