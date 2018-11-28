#include <iostream>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		unsigned long long N;
		cin >> N;
		bool digits[10] = {false};
		int count = 0;
		unsigned long long res = N;
		int j = 1;
		cout << "Case #" << i <<": ";
		while(true){
			unsigned long long tmp = res;
			while(tmp){
				int digit = tmp % 10;
				tmp /= 10;
				if(!digits[digit]){
					digits[digit] = true;
					count++;
				}
			}
			if(count == 10){
				cout << res << endl;
				break;
			}
			res = N * ++j;
			if(res == N){
				cout << "INSOMNIA" << endl;
				break;
			}
		}
	}
}