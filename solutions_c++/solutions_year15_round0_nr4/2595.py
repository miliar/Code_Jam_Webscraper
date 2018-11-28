#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main(){
	ifstream fin("D-small-attempt0.in");
	ofstream fout("outputD.txt");

	//Solutions for 1 <= X,R,C <= 4 were solved by hand

	int T;
	fin >> T;
	for (int t = 1; t <= T; t++){
		int X, R, C;
		fin >> X >> R >> C;
		string output;

		vector<map<pair<int, int>, string>> answers;
		auto x1 = map<pair<int, int>, string>();
		x1[make_pair(1, 1)] = "GABRIEL";
		x1[make_pair(2, 1)] = "GABRIEL";
		x1[make_pair(2, 2)] = "GABRIEL";
		x1[make_pair(3, 1)] = "GABRIEL";
		x1[make_pair(3, 2)] = "GABRIEL";
		x1[make_pair(4, 1)] = "GABRIEL";
		x1[make_pair(3, 3)] = "GABRIEL";
		x1[make_pair(4, 2)] = "GABRIEL";
		x1[make_pair(4, 3)] = "GABRIEL";
		x1[make_pair(4, 4)] = "GABRIEL";

		auto x2 = map<pair<int, int>, string>();
		x2[make_pair(1, 1)] = "RICHARD";
		x2[make_pair(2, 1)] = "GABRIEL";
		x2[make_pair(2, 2)] = "GABRIEL";
		x2[make_pair(3, 1)] = "RICHARD";
		x2[make_pair(3, 2)] = "GABRIEL";
		x2[make_pair(4, 1)] = "GABRIEL";
		x2[make_pair(3, 3)] = "RICHARD";
		x2[make_pair(4, 2)] = "GABRIEL";
		x2[make_pair(4, 3)] = "GABRIEL";
		x2[make_pair(4, 4)] = "GABRIEL";

		auto x3 = map<pair<int, int>, string>();
		x3[make_pair(1, 1)] = "RICHARD";
		x3[make_pair(2, 1)] = "RICHARD";
		x3[make_pair(2, 2)] = "RICHARD";
		x3[make_pair(3, 1)] = "RICHARD";
		x3[make_pair(3, 2)] = "GABRIEL";
		x3[make_pair(4, 1)] = "RICHARD";
		x3[make_pair(3, 3)] = "GABRIEL";
		x3[make_pair(4, 2)] = "RICHARD";
		x3[make_pair(4, 3)] = "GABRIEL";
		x3[make_pair(4, 4)] = "RICHARD";

		auto x4 = map<pair<int, int>, string>();
		x4[make_pair(1, 1)] = "RICHARD";
		x4[make_pair(2, 1)] = "RICHARD";
		x4[make_pair(2, 2)] = "RICHARD";
		x4[make_pair(3, 1)] = "RICHARD";
		x4[make_pair(3, 2)] = "RICHARD";
		x4[make_pair(4, 1)] = "RICHARD";
		x4[make_pair(3, 3)] = "RICHARD";
		x4[make_pair(4, 2)] = "RICHARD";
		x4[make_pair(4, 3)] = "GABRIEL";
		x4[make_pair(4, 4)] = "GABRIEL";

		answers.push_back(x1);
		answers.push_back(x2);
		answers.push_back(x3);
		answers.push_back(x4);

		output = answers[X-1][make_pair(max(C, R), min(C, R))];
		fout << "Case #" << t << ": " << output << endl;
	}
	fout.close();
	return 0;
}