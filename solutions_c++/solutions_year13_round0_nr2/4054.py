#include <iostream>
#include <string>
#include <vector>


using namespace std;




vector<int> splitD(string sent)
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



void readBox(vector<vector<int>> &box) {
	int N = box.size();
	int M = box[0].size();

	string readLine;
	for(int li = 0; li < N; ++li) {
		getline(cin, readLine);
		vector<int> line = splitD(readLine);
		for(int ri = 0; ri < M; ++ri)
			box[li][ri] = line[ri];
	}
}


int getLineMax(vector<vector<int>> &box, int li) {
	int M = box[li].size();
	int max = box[li][0];
	for(int ri = 1; ri < M; ++ri) {
		if(box[li][ri] > max)
			max = box[li][ri];
	}
	return max;
}


int getRowMax(vector<vector<int>> &box, int ri) {
	int N = box.size();
	int max = box[0][ri];
	for(int li = 1; li < N; ++li) {
		if(box[li][ri] > max)
			max = box[li][ri];
	}
	return max;
}


vector<int> getRowHeight(vector<vector<int>> &box) {
	int N = box.size();
	vector<int> hRow = vector<int>(N, 0);
	for(int li = 0; li < N; ++li)
		hRow[li] = getLineMax(box, li);
	return hRow;
}


vector<int> getLineHeight(vector<vector<int>> &box) {
	int M = box[0].size();
	vector<int> hLine = vector<int>(M, 0);
	for(int ri = 0; ri < M; ++ri)
		hLine[ri] = getRowMax(box, ri);
	return hLine;
}


bool replicates(vector<vector<int>> &box, vector<int> &hRow, vector<int>& hLine) {
	int N = box.size();
	int M = box[0].size();

	for(int li = 0; li < N; ++li) {
		for(int ri = 0; ri < M; ++ri) {
			if(box[li][ri] != min(hRow[li], hLine[ri]))
				return false;
		}
	}
	return true;
}



void printAnswer(int ti, bool achievable) {
	cout << "Case #" << ti << ": ";
	if(achievable)
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
}




int main()
{
	freopen("B-large.txt", "rt", stdin);
	freopen("out-B-large.txt", "wt", stdout);
	
	string readLine;

	// Number of tests
	int T;
	getline(cin, readLine);
	T = atof(readLine.c_str());
	
	for(int ti = 1; ti <= T; ++ti) {
		// N lines, M rows
		int N, M;
		getline(cin, readLine);
		vector<int> line = splitD(readLine);
		N = line[0];
		M = line[1];
		vector<vector<int>> lawn = vector<vector<int>>(N, vector<int>(M, 0));
		readBox(lawn);

		vector<int> hRow = getRowHeight(lawn);
		vector<int> hLine = getLineHeight(lawn);

		bool achievable = replicates(lawn, hRow, hLine);
		printAnswer(ti, achievable);

	}
	
	return 0;
}