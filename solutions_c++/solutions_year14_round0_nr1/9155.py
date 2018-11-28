#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
	ifstream in;
	in.open("A-small-attempt0.txt");
	int number;
	vector<int> list;
	int answer;
	int counter;
	int casenumber;
	string s;

	ofstream answerFile;
	answerFile.open("answer.txt");

	while (getline(in, s)) {
		stringstream line(s);
		string eachInt;
		while (line >> eachInt) {
			stringstream convert(eachInt);
			convert >> number;
			list.push_back(number);
		}
	}

	casenumber = list[0];

	for (int i = 1; i <= casenumber; i++) {
		answer = 0;
		counter = 0;
		for (int j = 4*(list[1]-1)+2; j < 4*(list[1]-1)+6; j++) {
			for (int k = 17+4*(list[18]-1)+2; k < 17+4*(list[18]-1)+6; k++) {
				if (list[j] == list[k]) {
					answer = list[k];
					counter++;
				}
			}
		} 
		if (counter == 0) {
			answerFile << "Case #" << i << ": Volunteer cheated!\r\n";
		} else if (counter == 1) {
			answerFile << "Case #" << i << ": " << answer << "\r\n";
		} else if (counter > 1) {
			answerFile << "Case #" << i << ": Bad magician!\r\n";
		}
		list.erase(list.begin()+1, list.begin()+35);
	}
	in.close();
	answerFile.close();
	
	return 0;
}



