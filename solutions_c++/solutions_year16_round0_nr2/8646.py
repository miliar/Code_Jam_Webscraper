#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int t;
	cin >> t;

	for(int i = 0; i < t; i++){
		string pc;
		cin >> pc;

		int maneuver = 0;

		bool signp = true; // Tracks continuous positive signs
		bool firstcase = true; // Tracks first case
		for(int j = 0; j < pc.length(); j++){
			if(pc[j] == '-'){
				
				while( j + 1 <= pc.length() && pc[j + 1] == '-'){ if(j == 0) signp = false; j++;}

				if((firstcase == true && signp == false) || j == 0){
					firstcase = false;
					maneuver += 1;
				} else maneuver += 2;
			}
			
		}

		cout << "CASE #" << i + 1 << ": " << maneuver << endl;
	}

	return 0;
}
