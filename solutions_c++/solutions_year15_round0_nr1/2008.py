#include <iostream>
using namespace std;

int T, M;

int main(){
	cin >> T;
	string digits;
	int count = 0;
	while(T--){
		cin >> M >> digits;
		int sum = 0;
		int need = 0;
		for(int i = 0; i <= M; i++){
			if(digits[i] == '0')
				continue;
			if(i > sum){
				need += i - sum;
				sum  = i + digits[i] - '0';
			}
			else{
				sum += digits[i] - '0';
			}
		}
		count++;
		cout << "Case #" << count << ": " << need << endl; 
	}
}