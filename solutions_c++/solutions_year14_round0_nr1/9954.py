#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <sstream>
using namespace std;

string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

string check(int a1[4][4], int a2[4][4], int ans_one, int ans_two) {
	// check if any entry in a1 at ans_one is equal to entries in a2 at ans_two
	// return strings
	int find_count = 0;
	int match = 0;
	for (int i=0;i<4;++i) {
		for (int j=0;j<4;++j) {
			if (a1[ans_one][i] == a2[ans_two][j]) {
				match = a1[ans_one][i];
				find_count++;
			}
		}
	}
	if (find_count == 0) {
		return "Volunteer cheated!";
	} else if (find_count == 1) {
		return convertInt(match);
	} else {
		return "Bad magician!";
	}
}



int main() {
	int case_one[4][4];
	int case_two[4][4];
	// 1 Get input (scanf %d) for number of cases
	// 2 Fill to num_cases
	int num_cases, result;
	int case_num = 1;
	std::string str_result = "";


	scanf("%d", &num_cases);
	while (num_cases != 0) { // Quits program when we decrement case # to 0
		// 3 Get the 'answer', fill to ans_case with scanf %d
		int ans_one;
		scanf("%d", &ans_one);
		// 4 Fill successive row arrays, fill using for loop and scanf %d
		for (int i=0;i<4;++i) {
			for (int j=0;j<4;++j) {
				scanf("%d", &case_one[i][j]); //420fillit
			}
		}

		// part two of the set
		int ans_two;
		scanf("%d", &ans_two);

		for (int i=0;i<4;++i) {
			for (int j=0;j<4;++j) {
				scanf("%d", &case_two[i][j]);
			}
		}

		str_result = check(case_one, case_two, (ans_one - 1), (ans_two - 1));


		printf("Case #%d: %s\n", case_num, str_result.c_str());

		case_num++;
		num_cases--;
	}
	return 0;
}
