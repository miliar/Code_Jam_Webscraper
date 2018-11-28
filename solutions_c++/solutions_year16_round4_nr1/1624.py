#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

vector<char> round(vector<char> in, int N, int n) {
	vector<char> out;
	for (int i = 0; i < in.size(); i++) {
		if (in[i] == 'P') {
			out.push_back('P');
			out.push_back('R');
		}
		else if (in[i] == 'R') {
			if (N == n) {
				out.push_back('R');
				out.push_back('S');
			}
			else {
				out.push_back('S');
				out.push_back('R');
			}
		}
		else {
			if (n < N - 1) {
				out.push_back('S');
				out.push_back('P');
			}
			else {
				out.push_back('P');
				out.push_back('S');
			}
		}
	}
	return out;
}

int main() {
	string file = "A-small-attempt1.in";
	ifstream input;
	input.open(file);
	ofstream output;
	output.open("out_" + file);
	int T;
	input >> T >> ws;
	for (int cases = 1; cases <= T; cases++)
	{
		output << "Case #" << cases << ": ";
		string line;
		getline(input, line);
		istringstream iss(line);
		
		int N; iss >> N;
		int R, P, S; iss >> R >> P >> S;

		vector<char> temp(1, 'P');
		for (int i = 1; i <= N; i++) {
			temp = round(temp, N, i);
		}
		int r = 0, p = 0, s = 0;
		for (int i = 0; i < temp.size(); i++) {
			if (temp[i] == 'P') p++;
			else if (temp[i] == 'R') r++;
			else s++;
		}
		if (r == R && p == P && s == S)
			for (int i = 0; i < temp.size(); i++) {
				output << temp[i];
			}
		else {
			temp.assign(1, 'R');
			for (int i = 1; i <= N; i++) {
				temp = round(temp, N, i);
			}
			int r = 0, p = 0, s = 0;
			for (int i = 0; i < temp.size(); i++) {
				if (temp[i] == 'P') p++;
				else if (temp[i] == 'R') r++;
				else s++;
			}
			if (r == R && p == P && s == S)
				for (int i = 0; i < temp.size(); i++) {
					output << temp[i];
				}
			else {
				temp.assign(1, 'S');
				for (int i = 1; i <= N; i++) {
					temp = round(temp, N, i);
				}
				int r = 0, p = 0, s = 0;
				for (int i = 0; i < temp.size(); i++) {
					if (temp[i] == 'P') p++;
					else if (temp[i] == 'R') r++;
					else s++;
				}
				if (r == R && p == P && s == S)
					for (int i = 0; i < temp.size(); i++) {
						output << temp[i];
					}
				else
					output << "IMPOSSIBLE";
			}
		}


		output << endl;
	}
	output.close();
	input.close();
	return 0;
}