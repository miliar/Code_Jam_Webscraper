#include <iostream>
#include <string>
using namespace std;

int n, smax;
string s;

int main(){

	cin >> n;
	for (int i = 0; i< n; i++){
		cin >> smax;
		cin >> s;
		int ans = 0;
		int curr = 0;
		for (int j = 0; j < smax + 1; j++){
			int c = s[j] - '0';
			if (curr < j && c != 0) {
				ans += j - curr;
				curr = j;
			}
			curr += c;
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}
