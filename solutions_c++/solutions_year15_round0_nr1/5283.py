
#include <stdlib.h>
#include <iostream>
#include <math.h>

using namespace std;

int* long_to_array(long a, int size){
	int* arr = new int[size + 1];
	for (int i = size; i >= 0; i--){
		long b = (pow(10, i));
		arr[size-i] = a / b;
		a = a % b;
	}
	return arr;
}

int main(){
	int test_case;
	cin >> test_case;
	for (int j = 1; j <= test_case; j++){
		int size;
		cin >> size;
		long a;
		cin >> a;
		int* arr = long_to_array(a, size);
		int total_people = 0;
		int total_needed = 0;
		for (int i = 0; i <= size; i++){
			if (i > total_people){
				total_needed += i - total_people;
				total_people += i - total_people;
			}
			total_people += arr[i];
		}
		cout << "Case #" << j << ": " << total_needed << endl;
		delete arr;

	}


	return 0;
}