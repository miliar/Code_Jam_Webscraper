#include <iostream>
using namespace std;
int S;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);


	int T;
	cin >> T;
	for (int i = 1; i <= T; i++){
		cin >> S;
		char str[1100] = {};
		cin >> str;
		int ans = 0;
		int sum = 0;
		for (int i = 0; i <= S; i++){
			int t = str[i] - '0';
			if (i > sum){
				ans += (i - sum);
				sum += (i - sum);
			}
			
			sum += t;
		}

		cout << "Case #" << i << ": " << ans << endl;
	}
	
	return 0;
}