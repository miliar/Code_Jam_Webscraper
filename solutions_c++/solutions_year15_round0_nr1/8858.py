#include <iostream>
#include <fstream>

using namespace std;

int main(){
	int T, S_MAX, upPeople, needFriends;
	char S[10000];
	ofstream fileOut;
	ifstream fileIn;
	
	fileIn.open("A-large.in", ios::binary);
	fileOut.open("A-largeOUT.in", ios::binary);

	fileIn >> T;

	for (int k = 1; k <= T; k++){
		fileIn >> S_MAX;

		fileIn >> S;

		needFriends = 0, upPeople = 0;

		for (int i = 0; i <= S_MAX; i++){
			if (upPeople >= i){
				upPeople += (S[i] - '0');
			}
			else{
				needFriends += (i - upPeople);
				upPeople = i + (S[i] - '0');
			}
		}
		
		fileOut << "Case #" << k << ": " << needFriends << endl;
	}
}