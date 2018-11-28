#include <iostream>

using namespace std;

int main(){

	int T;
	cin >> T;
	for(int t = 0 ; t<T; t++){
		int n;
		cin >> n;
		int sum = 0;
		int ans = -1;
		for(int i = 0; i <= n; i++){
			char x;
			cin >> x;
			int value = x-'0';
			int needed = i - sum;
			sum += value;
			ans = max(ans,needed);
		}
		cout << "Case #" << (t+1) <<": " << ans << endl; 
	}
	return 0;
}