#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

bool check(long long num, int &digits_seen){
	int digit=1;
	while(num>0){
		digit = 1 << num%10;
		digits_seen = digits_seen | digit;
		num-=num%10;
		num/=10;
	}
	if(digits_seen==1023) return true;
	return false;
}

int main(){
	int T;
	fin >> T;
	for(int t=0;t<T;t++){
		long long N;
		fin >> N;
		if(N==0){
			fout << "Case #" << t+1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		
		int digits_seen=0;
		long long num=0;
		for(long long i=1;;i++){
			num=i*N;
			if(check(num,digits_seen)) break;
		}
		
		fout << "Case #" << t+1 << ": " << num << endl;
		cout << "Case #" << t+1 << ": " << num/N << endl;
	}
	
	return 0;
}
