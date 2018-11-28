#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main(){

	int num_tests;
	int aud_size;
	char c;
	vector<char> shyness_levels;

	cin >> num_tests;
	for(int i=0; i<num_tests; i++){
		int friends = 0;
		int num_up = 0;
		cin >> aud_size;
		shyness_levels.clear();
		for(int j=0; j<=aud_size; j++){
			cin >> c;
			shyness_levels.push_back(c);
		}
		for(int j=0; j<=aud_size; j++){
			if(shyness_levels[j] != '0'){
				if(num_up >= j){
					;
				}
				else{
					friends += j-num_up;
					num_up += j-num_up;
					// cerr << "friends is now " << friends << "\n";
				}
			}
			num_up += (int)(shyness_levels[j]-'0');
		}
		cout << "Case #" << (i+1) << ": " << friends << "\n";
	}
	return 0;
}