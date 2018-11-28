#include <iostream>
#include <climits>
#include <fstream>
using namespace std;

typedef long long int ll;

void getDigits(ll N, bool* digit){
	while(N > 0){
		digit[N%10] = true;
		N /= 10;
	}
}

bool isFinalState(bool* digit){
	for(int i=0;i<10;i++){
		if(digit[i] == false) return false;
	}
	return true;
}

int main() {
	ll T,N,i,j,x,num;
	ifstream fin("input.in");
	ofstream fout("output.txt");
	fin>>T;
	for(i=1;i<=T;i++){
		fin>>N;
		if(N == 0){
			fout<<"Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		bool* digit= new bool[10];
		for(j=0;j<10;j++) digit[j] = false;
		x = 1;
		while(N < LONG_MAX/x && !isFinalState(digit)){
			getDigits(N * x, digit);
			x++;
		}
		fout<<"Case #"<<i<<": "<<N*(x-1)<<endl;
		delete[] digit;
	}
	return 0;
}
