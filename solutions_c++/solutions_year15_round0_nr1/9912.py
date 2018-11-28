#include <iostream>
#include <string>
using namespace std;

int countMissingAudience(string list, int S){
	if (S==0) return 0;
	
	int alreadyStanding= list.at(0)-'0';
	int count = 0;
	for (int i=1; i<=S; i++){
		if(alreadyStanding < i && list.at(i) != '0') {
			count+= i-alreadyStanding;
			alreadyStanding = i;
		}
		alreadyStanding += list.at(i)-'0';
	}
	return count;
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++){
		int S;
		string list;
		cin >> S;
		cin >> list;
		cout << "Case #" << i+1 <<": " << countMissingAudience(list, S) << endl;
	}
	return 0;
}
