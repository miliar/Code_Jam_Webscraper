#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solve(int length, string audience) {
	int clapper = 0;
	int invite = 0;

	for (int i=0; i<length; i++) {
		int current = audience[i] - '0';

		if (current == 0)
			continue;
		else if (i <= clapper) {
			clapper += current;
			//cout << "i: " << i << " current: " << current << " clapper: " << clapper << endl;
		} else {
			int newInvite = (i-clapper);

			invite += newInvite;
			clapper += newInvite;
			clapper += current;
			//cout << "i: " << i << " current: " << current << " invite: " << newInvite << " clapper: " << clapper << endl;
		}
	}
	return invite;
}

int main() {
	int T;

	cin >> T;
	//cout << "T: " << T << endl;
	for (int c=1; c<=T; c++) {
		int length, invite;
		string audience;

		cin >> length >> audience;
		//cout << "length: " << length << " audience: " << audience << endl;

		invite = solve(length+1, audience);
		cout << "Case #" << c << ": " << invite << endl;
	}

	return 0;
}