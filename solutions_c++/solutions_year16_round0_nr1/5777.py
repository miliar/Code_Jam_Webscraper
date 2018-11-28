#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;


int main(){
	int T, N, i = 1;
	long Y;
	bool can_sleep;
	cin >> T;
	cerr << "T: " << T << endl;

	for(int X = 1; X <= T; X++){
		int digits[][2] = {{0,0},{1,0},{2,0},{3,0},{4,0},{5,0},{6,0},{7,0},{8,0},{9,0}};
		cin >> N;
		if(N == 0){
			cout << "Case #" << X << ": " << "INSOMNIA" << endl;
			continue;
		}

		for( i = 1; i < 100; i++){
			Y = i * N;
			cerr<<"For N = "<< N <<", Y = "<< Y << endl;
			string number = to_string(Y);
			can_sleep = true;
			for(int count = 0; count < 10; count++){
				if(digits[count][1] == 0){
					if(number.find(to_string(digits[count][0])) != string::npos){
						digits[count][1] = 1;
					}else{
						can_sleep = false;
					}
				}
			}

			if(can_sleep){
				cout << "Case #" << X << ": "<< Y << endl;
				break;
			}	
		}
	}
	return 0;
}
