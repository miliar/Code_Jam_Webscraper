#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <time.h>
#define INPUTFILE "A-large.in"

using namespace std;
void countingSheep(int num, int testnum);

int main() {
	ifstream OpenFile(INPUTFILE);
	string ch;
	bool start = true;
	int size;
	vector<int> number;

	while (!OpenFile.eof())
	{
		getline(OpenFile,ch);
		if (start) {
			size = stoi(ch);
			start = false;
		}
		else {
			if (ch != "") number.push_back(stoi(ch));
		}
	}
	OpenFile.close();
	ofstream outFile("outFile.txt");
	
	int testcount = 1;
	for (vector<int>::iterator i = number.begin(); i != number.end(); i++) {
		bool fin = true;
		int count = 1;
		long long testnum;
		int arr[10] = { 0, };
		int starttime = clock();
		int endtime;
		int num = *i;
		while (fin) {
			testnum = num*count;
			do {
				int index = testnum % 10;
				arr[index] = 1;
				testnum /= 10;
			} while (testnum > 0);
			for (int i = 0; i < 10; i++) {
				if (arr[i] != 1) break;
				if (i == 9) fin = false;
			}
			count++;
			endtime = clock();
			if (endtime - starttime > 5 * CLOCKS_PER_SEC) break;
		}
		if (fin) outFile << "case #" << testcount << ": " << "INSOMNIA" << endl;
		else outFile << "case #" << testcount << ": " << num*(count - 1) << endl;
		testcount++;
	}
}