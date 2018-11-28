#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
using namespace std;
int main(void){
	ifstream testFile;
	ofstream outputFile;
	testFile.open("test.in.sdx",ios::in);
	outputFile.open("output.txt");
	string line;
	string row1;
	string row2;
	int r11,r12,r13,r14;
	int r21,r22,r23,r24;
	r11 = r12 = r13 = r14 = r21 = r22 = r23 = r24 = 0;
	int match1 = 0;
	int match2 = 0;
	getline(testFile, line);
	int numberOfCases = atoi(line.c_str());
	for (int i=0; i<numberOfCases; i++){
		// 10 Lines to read
		getline(testFile,line);
		int answer1 = atoi(line.c_str());
		for (int j=0; j<answer1; j++){
			getline(testFile,row1);
		}
		stringstream s1(row1);
		s1 >> r11 >> r12 >> r13 >> r14;
		for (int j=0; j<(4-answer1); j++){
			getline(testFile,line);
		}
		getline(testFile,line);
		int answer2 = atoi(line.c_str());
		for (int j=0; j<answer2; j++){
			getline(testFile,row2);
		}
		stringstream s2(row2);
		s2 >> r21 >> r22 >> r23 >> r24;
		for (int j=0; j<(4-answer2); j++){
			getline(testFile,line);
		}
		int arr[] = {r11, r12, r13, r14};
		int arr2[] = {r21, r22, r23, r24};
		vector<int> row1V(arr,arr+4);
		vector<int> row2V(arr2,arr2+4);
		
		for (int j=0; j<4; j++){
			if (!match1){
				if ((row1V[j] == row2V[0]) || (row1V[j] == row2V[1]) || (row1V[j] == row2V[2]) || (row1V[j] == row2V[3])){
					match1 = row1V[j];
					cout << "1 " <<  match1 << endl;
				}
			}
			else{
			if ((row1V[j] == row2V[0]) || (row1V[j] == row2V[1]) || (row1V[j] == row2V[2]) || (row1V[j] == row2V[3]))
					match2 = row1V[j];
			cout << "2 " << match2 << endl;
			}
		}
		if ((match1) && (!match2))
			outputFile << "Case #" << i+1 << ": " << match1 << endl;
		if ((match1) && (match2))
			outputFile << "Case #" << i+1 << ": Bad magician!" << endl;
		if ((!match1) && (!match2))
			outputFile << "Case #" << i+1 << ": Volunteer cheated!" << endl;
		match1 = 0;
		match2 = 0;
	}
	system("pause");  
}