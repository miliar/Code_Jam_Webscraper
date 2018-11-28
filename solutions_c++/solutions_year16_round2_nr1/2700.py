#include <fstream>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int getNumber(char S[], int num[]);
void countDown(int count[], int sum, char number[]);

int main() {
	//set input/output stream
	ifstream input;
	ofstream output;
	input.open("input.txt");
	output.open("output.txt");
	
	int T;
	char S[3000];
	int num[1000];
	
	input >> T;
	for(int x = 1; x <= T; x++) {
		input >> S;
		int len = getNumber(S, num);
		sort(num, num + len);
		//output
		output << "Case #" << x << ": ";
		for(int i = 0; i < len; i++) {
			output << num[i];
		}
		output << endl;
	}
	return 0;
}

int getNumber(char S[], int num[]) {
	int len = strlen(S);
	char numStr[20][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	int map[10] = {'Z', 'O', 'W', 'R', 'F', 'V', 'X', 'S', 'T', 'E'};
	int order[10] = {0, 6, 7, 5, 4, 3, 2, 1, 8, 9};
	//init count
	int count[300];
	for(int i = 0; i < 300; i++) {
		count[i] = 0;
	}
	for(int i = 0; i < len; i++){
		count[S[i]]++;
	}
	
	int sum = 0;
	for(int i = 0; i < 10; i++) {
		int ch = map[order[i]];
		if(count[ch] > 0) {
			for(int j = 0; j < count[ch]; j++) {
				num[sum++] = order[i];
			}	
			countDown(count, count[ch], numStr[order[i]]);
		}
	}


	return sum;
}	

void countDown(int count[], int sum, char number[]) {
	int len = strlen(number);
	while(sum > 0) {
		for(int i = 0; i < len; i++) {
			count[number[i]]--;
		}

		sum--;
	}
}
