#include <iostream>
using namespace std;

int main(){
	int T, t = 0, digit;
	long int N;
	cin >> T;

	for(int counter = 0; counter < T; counter++){
		cin >> N;
		long int A = N;
		int digits[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, check = 0, at = 2;
		while(!(digits[0] * digits[1] * digits[2] * digits[3] *digits[4] * digits[5] * digits[6] * digits[7] * digits[8] * digits[9]) && (check < 10000)){
		    A = N;
			while(A > 0){
				digit = A % 10;
				if(!(digits[digit]))
					digits[digit]++;
				A = A/10;
			}
			N = (N * at) / (at-1);
			check++;
			at++;
		}
		
		if(digits[0] * digits[1] * digits[2] * digits[3] *digits[4] * digits[5] * digits[6] * digits[7] * digits[8] * digits[9]){
			cout << "Case #" << t+1 << ": " << ((N * (at-2)) / (at-1)) << endl;
			t++;
		}
		
		else{
		    cout << "Case #" << t+1 << ": " << "INSOMNIA" << endl;
		    t++;
		}
		at = 0;
	}
	return 0;
}