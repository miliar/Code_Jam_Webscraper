#include <bits/stdc++.h>

using namespace std;

string expand(string start, int n) {
	while (n) {
		string next="";
		for (auto c : start) {
			switch(c) {
			case 'P':
				next += "PR";
				break;
			case 'R':
				next += "RS";
				break;
			case 'S':
				next += "PS";
				break;
			}
		}
		start = next;
		n--;
	}
	return start;
}

bool cmp(string &cur, int la, int ha, int lb, int hb) {
	while (la < ha) {
		if (cur[la] > cur[lb]) return true;
		if (cur[la] < cur[lb]) return false;
		la++;
		lb++;
	}
	return false;
}

void sort(string &cur, int low, int high) {
	if (high - low == 2) {
		if (cur[low] > cur[low+1]) swap(cur[low], cur[low+1]);
		return;
	}
	
	if (high - low < 2) return;
	
	int mid = (high+low)/2;
	sort(cur, low, mid);
	sort(cur, mid, high);
	
	if (cmp(cur, low, mid, mid, high)) {
		for (int i=0; i<mid-low; i++) {
			swap(cur[low+i], cur[mid+i]);
		}
	}
}

void doCase(int t) {
	int N, P, R, S;
	cin >> N >> R >> P >> S;
	
	string cP = expand("P", N);
	string cR = expand("R", N);
	string cS = expand("S", N);
	
	int count[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
	
	for (int i=0; i<(1<<N); i++) {
		switch(cP[i]) {
		case 'P':
			count[0][0]++;
			break;
		case 'R':
			count[0][1]++;
			break;
		case 'S':
			count[0][2]++;
			break;
		}
		switch(cR[i]) {
		case 'P':
			count[1][0]++;
			break;
		case 'R':
			count[1][1]++;
			break;
		case 'S':
			count[1][2]++;
			break;
		}
		switch(cS[i]) {
		case 'P':
			count[2][0]++;
			break;
		case 'R':
			count[2][1]++;
			break;
		case 'S':
			count[2][2]++;
			break;
		}
	}
	
	if (count[0][0] != P || count[0][1] != R || count[0][2] != S) cP = "";
	if (count[1][0] != P || count[1][1] != R || count[1][2] != S) cR = "";
	if (count[2][0] != P || count[2][1] != R || count[2][2] != S) cS = "";
	
	sort(cP, 0, cP.size());
	sort(cR, 0, cR.size());
	sort(cS, 0, cS.size());
	
	vector<string> cands;
	if (cP.size() != 0) cands.push_back(cP);
	if (cR.size() != 0) cands.push_back(cR);
	if (cS.size() != 0) cands.push_back(cS);
	
	sort(cands.begin(), cands.end());
	cout << "Case #" << t << ": ";
	if (cands.size() == 0) {
		cout << "IMPOSSIBLE" << endl;
	} else {
		cout << cands[0] << endl;
	}
}

int main () {
	int t;
	cin >> t;
	for (int i=0; i<t; i++) doCase(i+1);
	return 0;
}
