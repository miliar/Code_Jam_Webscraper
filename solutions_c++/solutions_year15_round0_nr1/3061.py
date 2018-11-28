#include "StandingOvation.h"

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++){
		int slMax = 0;
		string slCounts;
		cin >> slMax;
		cin >> slCounts;
		int result = StandingOvation().minFriends(slMax, slCounts);
		cout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}
