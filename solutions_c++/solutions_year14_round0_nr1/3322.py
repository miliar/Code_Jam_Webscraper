// magic trick in google code jam 2014
#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;

const string CASE = "Case #";
const string BAD = "Bad magician!";
const string CHEATED = "Volunteer cheated!";

const int BAD_ANSWER = -1;
const int CHEATED_ANSWER = -2;

// guess an answer for magic trick
int guess(int case_num,fstream &file1) {
	int first_answer;
	int second_answer;
	int first_arrange[16];
	int second_arrange[16];

	file1 >> first_answer;
	for (int i = 0; i < 16; i++) {
		file1 >> first_arrange[i];
	}

	file1 >> second_answer;
	for (int i = 0; i < 16; i++) {
		file1 >> second_arrange[i];
	}

	int found[4] = {0};
	int num[4] = {0};

	for (int i = 0; i < 4; i++) {
		int cardNum = first_arrange[4*(first_answer-1) + i];
		for (int j = 0; j < 16; j++) {
			if (cardNum == second_arrange[j]) {
				found[j/4]++;
				num[j/4] = cardNum;
			}
		}
	}

	if (found[second_answer-1] == 0) {
		return CHEATED_ANSWER;
	}
	if (found[second_answer-1] > 1) {
		return BAD_ANSWER;
	}
	return num[second_answer-1];


}
int main() {

	int T; // number of test cases
	fstream file1;
	file1.open("e:\\A-small-attempt0.txt",ios::in);
	fstream file2;
	file2.open("e:\\a-attempt0-out.txt",ios::out);
	file1 >> T;
	cout<<T<<endl;
	for (int i = 0; i < T; i++) {
		int a = guess(i+1,file1);
		switch(a) {
			case BAD_ANSWER:
				file2 << "Case #";
				file2 << (i+1); 
				file2 <<": ";
				file2 << "Bad magician!";
				file2 << endl;	
				break;
			case CHEATED_ANSWER:
				file2 << "Case #";
				file2 << (i+1); 
				file2 <<": ";
				file2 << "Volunteer cheated!";
				file2 << endl;		
				break;
			default:
				file2 << "Case #";
				file2 << (i+1); 
				file2 <<": ";
				file2 << a;
				file2 << endl;			
				break;
		}
	}
}

