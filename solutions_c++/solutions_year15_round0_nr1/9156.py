#include <iostream>

using namespace std;

int t, n, sum = 0, res = 0;
string s;

int main(){

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;

	for(int q = 0; q < t; ++q){
		cin >> n >> s;
		sum = int(s[0] - '0');
		res = 0;
		
		for(int i = 1; i < s.size(); ++i){
			if(sum < i) res += i - sum, sum += i - sum;
			sum += int(s[i] - '0');
		}

		cout << "Case #" << q + 1 << ": " << res << endl;
	}

	return 0;
}