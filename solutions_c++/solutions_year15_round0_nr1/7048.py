#include <iostream>
using namespace std;

char adce[1005];

int main(){

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t, n, sum, result;

	cin >> t;

	for (int i = 1; i <= t; i++){
		cin >> n >> adce;
		result = sum = 0;
		for (int j = 0; j <= n; j++){
			if (sum + result < j) result += (j - sum - result);
			sum += (adce[j] - 48);
		}
		cout << "Case #" << i << ": " << result << endl;
	}


	return 0;
}