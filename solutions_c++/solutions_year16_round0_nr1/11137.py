#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <map>
#include <cmath>

using namespace std;


void change_digits(int N, int *digits){
	int d;
	while ( N !=0  ){
		d= N%10;
		digits[d] =1;
		N= N/10;
	}
		// for(int i=0; i< 0; i++){
		// 	cout << digits[i];
		// }
}



int digits_check( int* digits){
	int i;
	for(int i =0; i< 10; i++){
		if (digits[i]==0)
		return 1;
	}
	return 0 ;
}



int find_result(int N){

	int digits[10];
	for(int i = 0; i < 10; i++) {
		digits[i]=0;
	}
	if (N == 0)
		return -1;
	int k =1;
 	while(digits_check(digits)){ 
 		change_digits(k*N, digits); 
		k++;
	}
	return (k -1)*N;
}


int main(int argc, const char *argv[]) {
	int T,N;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int result = 0;
		cin >> N;
		// cout	<< N;
		result = find_result(N);
		if (result == -1)
			cout << "Case #" << i +1  << ": " << "INSOMNIA" << "\n";
		else
			cout << "Case #" << i +1  << ": " << result << "\n";
	}
	return 0;
}
