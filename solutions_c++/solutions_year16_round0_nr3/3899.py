// QuestionA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <bitset>

using namespace std;

#define CURR_N 16

long long convertFromBits(string number, int base){
	long long curr_num = 0;
	for (long long bit_in_binary = 0; bit_in_binary < CURR_N; bit_in_binary++){
		curr_num += ((long long)(number[bit_in_binary] - '0'))*((long long)pow(base, (CURR_N - bit_in_binary - 1)));
	}
	return curr_num;
}

long long findLowerDivider(long long number){
	for (int i = 2; i <= sqrt(number); i++){
		if ((number % i) == 0){
			return i;
		}
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++){
		cout << "Case #" << i << ":" << endl;
		int N, J;
		cin >> N >> J;
		int found = 0;
		for (long long j = 0; j <= 4095; j++){
			string curr_num_in_string = "1" + bitset<CURR_N-2>(j).to_string() + "1";
			string string_to_print = curr_num_in_string + " ";
			
			for (int base = 2; base <= 10; base++){
				long long curr_num = convertFromBits(curr_num_in_string, base);
				long long lower_divider = findLowerDivider(curr_num);
				if (lower_divider == 0){
					string_to_print = "";
					break;
				}else{
					string_to_print += to_string(lower_divider);
					if (base != 10){
						string_to_print += " ";
					}
				}
			}
			if (string_to_print != ""){
				cout << string_to_print << endl;
				found++;
			}




			if (found >= J){
				break;
			}
		}


		cin >> T; // TODO DELETE
	}
	return 0;
}

