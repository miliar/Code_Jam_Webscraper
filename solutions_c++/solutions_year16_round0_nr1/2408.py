#include <iostream>
#include <fstream>
using namespace std;

int digits[10] = {0,0,0,0,0,0,0,0,0,0};
int last_digit = -4343;


int digits_check(long int n) {
	long int nmbr=n, digit = 0;
	int flag=1;
	while(nmbr!=0) {
		digit = nmbr%10;
		if(digit == 0) {
			digits[0] =1;
		}
		if(digits[digit]==0) {
			digits[digit] = 1;
		}
		nmbr/=10;
	}

	for(int j=0; j<10; j++) {
		flag = flag && digits[j];
	}
	if(flag) {
		last_digit = n;
		return 1;
	} 
	else {
		return 0;
	}
}

int main() {
	ofstream output;
	output.open("output.txt");

	long int T,N;

	cin>>T;

	for(int t=0;t<T;t++){
		for(int j=0; j<10; j++) {
			digits[j] = 0;
		}
		cin>>N;
		long int t_N = N;
		long int i=1;
		if(N==0) {
			output<<"Case #"<<(t+1)<<": INSOMNIA"<<endl;
		} else {
			while(true) {
				if(digits_check(N)) {
					output<<"Case #"<<(t+1)<<": "<<last_digit<<endl;
					last_digit = -4343;
					break;
				} else {
					i=i+1;
					N=t_N*i;
				}
			}
			
		}
	}

	output.close();
	return 0;
}