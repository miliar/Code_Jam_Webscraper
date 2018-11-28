#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

	string line;
	ifstream inFile("in.txt");
	ofstream outFile("out.txt");
	getline(inFile, line);
	int T = stoi(line);
	int cnt = T;
	int result;

	int N, num;
	while (cnt-- && getline(inFile, line)) {

		map<int, int> mapD;
		mapD.clear();
		vector<int> num;

		int L = line.length();
		for (int i = 0; i < L; i++) {
			mapD[(line.at(i) - 'A' + 1)] ++;
		}

		while (mapD[7] > 0) {
			mapD[5]--; mapD[7]--; mapD[8]--; mapD[9]--; mapD[20]--;
			num.push_back(8);
		}
		while (mapD[26] > 0) {
			mapD[5]--; mapD[15]--; mapD[18]--; mapD[26]--;
			num.push_back(0);
		}
		while (mapD[23] > 0) {
			mapD[15]--; mapD[20]--; mapD[23]--;
			num.push_back(2);
		}
		while (mapD[21] > 0) {
			mapD[6]--; mapD[15]--; mapD[18]--; mapD[21]--;
			num.push_back(4);
		}
		while (mapD[24] > 0) {
			mapD[9]--; mapD[19]--; mapD[24]--;
			num.push_back(6);
		}
		while (mapD[20] > 0) {
			mapD[5]-=2; mapD[8]--; mapD[18]--; mapD[20]--;
			num.push_back(3);
		}
		while (mapD[19] > 0) {
			mapD[5] -= 2; mapD[14]--; mapD[19]--; mapD[22]--;
			num.push_back(7);
		}
		while (mapD[19] > 0) {
			mapD[5] -= 2; mapD[14]--; mapD[19]--; mapD[22]--;
			num.push_back(7);
		}
		while (mapD[22] > 0) {
			mapD[5] --; mapD[6]--; mapD[9]--; mapD[22]--;
			num.push_back(5);
		}
		while (mapD[15] > 0) {
			mapD[5] --; mapD[14]--; mapD[15]--;
			num.push_back(1);
		}
		while (mapD[9] > 0) {
			mapD[5] --; mapD[9]--; mapD[14]--;
			num.push_back(9);
		}

		sort(num.begin(), num.end());

		outFile << "Case #" << T - cnt << ": ";
		for (int i = 0; i < num.size(); i++) {
			outFile << num[i];
		}
		outFile << endl;

		/*
		//G	7	EIGHT			5	7	8	9	20
		//Z	26	ZERO			5	15	18	26
		//W	23	TWO				15	20	23
		//U	21	FOUR			6	15	18	21
		//X	24	SIX				9	19	24
		//T	20	THREE			8	18	20	5(2)
		//S	19	SEVEN			14	19	22	5(2)
		//V	22	FIVE			5	6	9	22
		//O	15	ONE				5	14	15
		//I	9	NINE		    5	9	14(2)
		*/
	}

	return 0;
}