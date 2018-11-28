#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

class Node {
	Node* next[26];
public:
	Node() {
		fill(next, next + 26, (Node*) NULL);
	}

	~Node() {
		for (int i = 0; i < 26; i++) {
			if (next[i]) 
				delete next[i];
		}
	}

	void add(const string& s, const int pos = 0) {
		int idx = s[pos] - 'A';
		if (next[idx] == NULL)
			next[idx] = new Node();
		if (pos + 1 < s.length())
			next[idx]->add(s, pos + 1);
	}

	int numNodes() {
		int k = 1;
		for (int i = 0; i < 26; i++) {
			if (next[i])
				k += next[i]->numNodes();
		}
		return k;
	}
};

int count(const vector<string>& s, vector<int>& serverIdx, int n) {
	vector<Node> tries(n);
	for (int i = 0; i < s.size(); i++) 
		tries[serverIdx[i]].add(s[i]);

	int k = 0;
	for (int i = 0; i < n; i++) {
		int t = tries[i].numNodes();
		if (t > 1)
			k += t;
	}
	return k;
}

void run(const vector<string>& s, int t, vector<int>& serverIdx, int n, int& maxVal, int& maxCnt) {
	if (t == s.size()) {
		int k = count(s, serverIdx, n);
		if (k > maxVal) {
			maxVal = k;
			maxCnt = 1;
		} else if (k == maxVal)
			maxCnt++;
		return;
	}

	for (int i = 0; i < n; i++) {
		serverIdx[t] = i;
		run(s, t + 1, serverIdx, n, maxVal, maxCnt);
	}
}

int main() {
	fstream fin("D-small-attempt1.in");
	ofstream fout("out.txt");
	istream& in = fin;
	ostream& out = fout;
	int T;
	in >> T;
	for (int test_case = 1; test_case <= T; test_case++) {
		cout << test_case << endl;
		int m, n;
		in >> m >> n;
		vector<string> s(m);
		for (int i = 0; i < m; i++) in >> s[i];
		int maxVal = 0, maxCnt = 0;
		vector<int> serverIdx(m);
		run(s, 0, serverIdx, n, maxVal, maxCnt);
		out << "Case #" << test_case << ": " << maxVal << " " << maxCnt << endl;
	}

	return 0;
}
