// GCJ2015
// A Standing Ovation

#include <iostream>
#include <string>
using namespace std;

int main() {
	int T, testcase;
	cin >> T;
	for (testcase=1;testcase<=T;testcase++) {
		int Smax, ans=0, standing=0;
		string S;
		cin >> Smax >> S;
		for (int i=0; i<Smax+1; i++) {
			if (standing < i) {
				ans += i - standing;
				standing = i;
			}
			standing += S[i]-'0';
		}
		cout << "Case #" << testcase << ": " << ans << endl;
	}
	return 0;
}
