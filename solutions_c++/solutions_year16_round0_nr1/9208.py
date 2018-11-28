#include <iostream>
using namespace std;

typedef unsigned long long ui;

int main(){

	ui T = 0;
	cin >> T;
	ui N = 0;
	ui case_num = 1;

	while(T--){

		ui bucket[10] = {0};
		ui num_digit_seen = 0;
		ui temp = 0, temp2 = 0;	

		cin >> N;

		if(N==0){
			cout << "Case #" << case_num <<": INSOMNIA" << endl;
		}
		else{
			temp = 0;
			while(num_digit_seen != 10){
				temp = temp+N;
				temp2 = temp;
				while(temp2!=0){
					int mod = temp2%10;
					if(bucket[mod]==0){
						bucket[mod]=1;
						num_digit_seen++;
					}
					temp2 = temp2/10;
				}
			}
			cout << "Case #" << case_num <<": " << temp << endl;	
		}
		case_num++;
	}

	return 0;
}
