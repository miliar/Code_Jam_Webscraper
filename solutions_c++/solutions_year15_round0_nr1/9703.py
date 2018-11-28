#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[]){

	int tests;
	cin >> tests;

	for(int t = 0; t < tests; t++){
		int maxS;
		cin >> maxS;
		int friends = 0;
		int standing = 0;
		string inp;
		getline(cin, inp);

		for(int i = 1; i <= maxS + 1; i++){
			if(standing < i - 1){
				friends++;
				standing++;
			}
			int tmp = inp.at(i) - '0';
			standing += tmp;
		}
		cout << "Case #" << t + 1 << ": " << friends << endl;
	}

	return 0;
}
