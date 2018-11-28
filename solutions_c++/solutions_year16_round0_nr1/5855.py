#include <iostream>
using namespace std;

int T;
long long int N;
int digits[10];

bool repeat() {
	for(int i = 0; i<10; i++) {
		if(digits[i] == 0) return true;
	}
	return false;
}

void add(int N) {
	while(N>0) {
		digits[N%10]++;
		N/=10;
	}
}

void clearDigits() {
	for(int i = 0; i<10; i++) digits[i] = 0;
}

int main() {
	cin>>T;

	for(int j=1; j<=T; j++) {
		clearDigits();
		cin>>N;
		if(N==0) {
			cout<<"Case #"<<j<<": INSOMNIA\n";
		}
		else {
			long long int i=1;
			while( repeat() ) {
				add(i*N);
				i++;
			}
			cout<<"Case #"<<j<<": "<<N*(i-1)<<"\n";
		}
	}
	
	return 0;
}

