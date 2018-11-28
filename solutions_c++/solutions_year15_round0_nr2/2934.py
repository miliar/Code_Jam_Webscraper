#include "InfiniteHouseofPancakes.h"

int main(){
	int T;
	cin >> T;
	int res[1001];
	for (int i = 1; i <= T; i++){
		int n;
		cin >> n;
		for (int m = 1; m <= n; m++){
			cin >> res[m];
		}
		int result = InfiniteHouseofPancakes().finishBreakfast(n, res);
		cout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}
