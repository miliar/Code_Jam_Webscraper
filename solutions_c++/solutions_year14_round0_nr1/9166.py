#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
#include <queue>
#include <string>
#include <math.h>
#define DEBUG 1
#define LOG(x) if(DEBUG) cout << x << endl
using namespace std;

int main() {
	ifstream in;
	in.open("A-small-attempt2.in", ios::in);
	ofstream out;
	out.open("A-small.out", ios::out);
	int t;
	in >> t;
	for(int i = 0; i < t; i++) {
		int r0;
		in >> r0;
		r0--;
		vector<int> answers;
		bool valid[16];
		memset(valid, 0, 16 * sizeof(bool));
		for(int j = 0; j < 16; j++) {
			int temp;
			in >> temp;
			if(j >= r0 * 4 && j < (r0 + 1) * 4)
				valid[temp - 1] = true;
		}
		int r1;
		in >> r1;
		r1--;
		for(int j = 0; j < 16; j++) {
			int temp;
			in >> temp;
			if(j >= r1 * 4 && j < (r1 + 1) * 4 && valid[temp-1])
				answers.push_back(temp);
		}
		
		out << "Case #" << (i+1) << ": ";
		if(answers.size() == 1) {
			out << answers[0] << endl;
		} else if(answers.size() > 1) {
			out << "Bad magician!" << endl;
		} else {
			out << "Volunteer cheated!" << endl;
		}
		
	}
	in.close();
	out.close();
}