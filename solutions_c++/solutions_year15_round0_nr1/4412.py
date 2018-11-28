#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main(){

	int t, smax, minFriends, standing;
	char buffer;
	string str;

	cin >> t;

	for(int tt = 1; tt <= t; tt++){
		minFriends = 0;
		cin >> smax >> str;
		standing = str[0] - '0';
		for(int dd = 1; dd <= smax; dd++){
			if(dd - standing > 0){
				minFriends += (dd-standing);
				standing = dd;
			}
			standing+=str[dd] - '0';
		}
		cout << "Case #" << tt << ": " << minFriends << endl;
	}

	return 0;

	return 0;
}