#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;

vector<int> phonenum(string& s) {
	int ht[26] = { 0 };
	int num[10] = { 0 };
	int n = s.length();
	for (int i = 0; i < n; i++) {
		ht[s[i] - 65]++;
	}

	num[0] = ht[25];
	num[2] = ht[22];
	num[4] = ht[20];
	num[6] = ht[23];
	num[8] = ht[6];
	num[5] = ht[5] - num[4];
	num[5] = (num[5] > 0) ? num[5] : 0;
	num[7] = ht[21] - num[5];
	num[7] = (num[7] > 0) ? num[7] : 0;
	num[3] = ht[17] - num[0] - num[4];
	num[3] = (num[3] > 0) ? num[3] : 0;
	num[9] = ht[8] - num[5] - num[6] - num[8];
	num[9] = (num[9] > 0) ? num[9] : 0;
	num[1] = ht[14] - num[0] - num[2] - num[4];
	num[1] = (num[1] > 0) ? num[1] : 0;

	vector<int> result;
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < num[i]; j++) {
			result.push_back(i);
		}
	}

	return result;
}



void main() {
	fstream infile, outfile;
	int testnum;
	string s;
	infile.open("A-large.in", ios::in);
	outfile.open("output.dat", ios::out);
	infile >> testnum;
	getline(infile, s);
	vector<int> result;
	for (int i = 1; i <= testnum; i++) {
		getline(infile, s);
		result = phonenum(s);
		outfile << "Case #" << i << ": ";
		for (int j = 0; j < result.size(); j++) {
			outfile << result[j];
		}
		outfile << '\n';
	}
}