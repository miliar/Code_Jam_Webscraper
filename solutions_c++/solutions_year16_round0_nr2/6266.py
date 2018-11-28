#include <iostream>
using namespace std;

int main(){

	int t;
	cin >> t;

	for(int i = 1;i <= t;i++){
		string s;

		cin >> s;
		int step = 0;
		bool state;

		for(int j = 0;j < s.length();j++){
			if(j == 0){
				if(s[j] == '+')
					state = true;
				else
					state = false;

				continue;
			}

			if(state){
				if(s[j] == '+'){
					continue;
				}
				else{
					step++;
					state = false;
				}
			}
			else{
				if(s[j] == '-'){
					continue;
				}
				else{
					step++;
					state = true;
				}
			}
		}

		if(state == false){
			step++;
		}

		cout << "Case #" << i << ": " << step << endl;
	}

	return 0;
}