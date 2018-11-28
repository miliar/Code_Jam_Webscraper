#define _USE_MATH_DEFINE
#include <cmath>
#include <iostream>

using namespace std;

long calculate(const long radius, long t);

int main(void){
	int testCases;
	cin >> testCases;
	for(int i = 1; i <= testCases; i++){
		int r,t;
		cin >> r >> t;
		long int result = calculate(r,t);
		cout << "Case #" << i << ": " << result << endl;
	}
	return 0;
}

long calculate(const long radius, long t){
	long int result = 0;
	for(long int i = 0;; i+=2){
		long int inner = radius + i;
		long int outer = inner + 1;
		long int area = ( (outer*outer) - (inner*inner) );
		t -= area;
		if(t < 0){
			return result;
		}
		result++;
	}
	return result;
}
