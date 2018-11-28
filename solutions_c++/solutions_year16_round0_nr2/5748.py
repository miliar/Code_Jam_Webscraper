#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	int T;
	cin >> T;

	for(int i=1; i<=T; i++){
		string pancakes;
		cin >> pancakes;

		int groups = 0;
		char prev = '0';
		for(int i=0; i<pancakes.size(); i++){
			if(prev != pancakes[i]){
				groups++;
				prev = pancakes[i];
			}
		}

		if(pancakes[0] == '+'){
			if(groups%2 == 1){
				groups--;
			}
		}
		else{
			if(groups%2 == 0){
				groups--;
			}
		}

		printf("Case #%d: %d\n", i, groups);
	}

	return 0;
}
