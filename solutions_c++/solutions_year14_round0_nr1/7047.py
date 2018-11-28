#include <iostream>
#include <string>
#include <vector>
#include <math.h>


using namespace std;
typedef vector<vector<int>> VV;


void dPause() {
	int j = 0;
	++j;
	return;
}


vector<int> split(string sent)
{
	if(sent.size() < 1)
		return vector<int>();
	vector<int> answer;
	
	int start = 0, end = 0;
	char delim = ' ';
	
	while( (end = sent.find(delim, start)) != string::npos) {
		string curSubstr = sent.substr(start, end-start);
		if(curSubstr.size() > 0)
			answer.push_back(atof(curSubstr.c_str()));
		start = end + 1;
	}
	string endSubstr = sent.substr(start, sent.size()-start);
	if(endSubstr.size() > 0)
		answer.push_back(atof(endSubstr.c_str()));
	return answer;
}



vector<vector<int>> readMatrix(unsigned u_size) {
	vector<vector<int>> matrix = vector<vector<int>>(u_size, vector<int>());
	string readLine;
	for(unsigned i = 0; i < u_size; ++i) {
		getline(cin, readLine);
		matrix[i] = split(readLine);
	}
	return matrix;
}


int compare(vector<int> u_row1, vector<int> u_row2) {
	// 0 if no matches
	// ans if 1 match
	int ans = 0;
	unsigned matches = 0;
	for(int i = 0; i < u_row1.size(); ++i) {
		for(int j = 0; j < u_row2.size(); ++j) {
			if(u_row1[i] == u_row2[j]) {
				ans = u_row1[i];
				++matches;
			}
		}
	}
	//-1 if more then 1 match
	if(matches > 1)
		ans = -1;
	return ans;
}




void printResult(int ti, int ans) {
	switch(ans) {
		case 0:
			cout << "Case #" << ti << ": Volunteer cheated!" << endl;
			break;
		case -1:
			cout << "Case #" << ti << ": Bad magician!" << endl;
			break;
		default:
			cout << "Case #" << ti << ": " << ans << endl;
	}
}




int main()
{
	freopen("A-small-attempt1.in", "rt", stdin);
	freopen("out-A-small-attempt1.txt", "wt", stdout);
	
	string readLine;

	// Number of tests
	int T;
	getline(cin, readLine);
	T = atof(readLine.c_str());
//	cin >> T;
	
	for(int ti = 1; ti <= T; ++ti) {
		unsigned r1, r2;
		VV matr1, matr2;

		getline(cin, readLine);
		r1 = atof(readLine.c_str());
		matr1 = readMatrix(4);
		getline(cin, readLine);
		r2 = atof(readLine.c_str());
		matr2 = readMatrix(4);

		int ans = compare(matr1[r1 - 1], matr2[r2 - 1]);
		printResult(ti, ans);
		dPause();
	}


	dPause();
	return 0;
}