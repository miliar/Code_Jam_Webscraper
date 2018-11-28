#include <iostream>
using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false);
	short T, Smax, count = 1;
	cin >> T;
	for(string S; cin >> Smax >> S; count++) {
		short standing = 0, friends = 0;
		for(auto i = 0; i != S.size(); i++) {
			if(standing < i) {
				friends += i - standing;
				standing += i - standing;
			}
			standing += S[i] - '0';
		}
		cout << "Case #" << count << ": " << friends << endl;
	}
	return 0;
}