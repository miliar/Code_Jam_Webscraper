/*
 * source.cpp
 *
 *  Created on: Apr 8, 2016
 *      Author: Lesly
 */

#include <iostream>
#include <vector>

using namespace std;

long long function1(long long n){
	vector <bool> myVector;
	for (int i = 0; i < 10; i++){
			myVector.push_back(true);
	}

	long long i = 1;
	bool keepGoing = true;
	while(keepGoing){
		long long p = n * i;
		while(p != 0){
			if (myVector [p % 10]){
				myVector [p % 10] = false;
			}
			p /= 10;
		}


		for(int iter = 0; iter <= 9; iter++){
			if(myVector[iter]) break;
			if(!myVector[iter] && iter == 9 ){
				keepGoing = false;
			}
		}
		i++;
	}

	return n * (i - 1);
}


int main(){
	int t = 0;

	cin >> t;
	int i = 1;
	while(i <= t){
		long long n = 0;
		cin >> n;


		if (n == 0){
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		}
		else{
			cout << "Case #" << i << ": " << function1(n) << endl;
		}

		i++;
	}

	return 0;
}



