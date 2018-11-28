#include <iostream>
#include <vector>
using namespace std;

int main(){
	int cases;
	string pancakes;
	cin >> cases;
	++cases;
	for(int c = 1; c < cases; ++c){
		cin >> pancakes;
		int length = pancakes.length();

		if(length == 1){
			if(pancakes.at(0) == '+'){
				cout << "Case #" << c << ": " << 0 << '\n';
			}
			else{
				cout << "Case #" << c << ": " << 1 << '\n';
			}
			continue;
		}

		vector<bool> pancakeStack(length, false);
		for(int i = 0; i < length; ++i){
			if(pancakes.at(i) == '+'){
				pancakeStack[i] = true;
			}
		}

		int flipCount = 0;
		int i = 1;
		while(i < length){
			if(pancakeStack[0] == pancakeStack[i]){
				++i;
			}
			else{
				for(int j = 0; j < i; ++j){
					pancakeStack[j] = !pancakeStack[j];
				}
				++flipCount;
			}
		}

		if(!pancakeStack[0]) ++flipCount;
		cout << "Case #" << c << ": " << flipCount << '\n';
	}
	return 0;
}