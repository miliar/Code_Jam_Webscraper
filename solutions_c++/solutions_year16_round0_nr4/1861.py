#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string makeString (int l, int p);
string makeBigString (string original, int times, int size);

int main () {
	int T, K, C, S, numPts, groupNum, num, i, j, k, flag;
	unsigned long long int position, maxNum;
	vector<unsigned long long int> vp;
	string s;
	
	cin >> T;
	
	for (i=1;i<=T;i++) {
		cin >> K >> C >> S;
		maxNum = pow(K, C);
		//cout << "maxnum " << maxNum << endl;
		numPts = ceil(float(K)/float(C));
		vp.clear();
		
		//cout << "Number of pts: " << numPts << endl;
		
		if (numPts > S) {
			cout << "Case #" << i << ": IMPOSSIBLE" << endl;
			continue;
		}
		
		position = 0;
		cout << "Case #" << i << ":";
		for (j=0;j<K;j++) {
			cout << " " << position + 1;
			position = position + pow(K, C-1);
		}
		cout << endl;
		
		/*
		position = 0;
		groupNum = 0;
		cout << "Case #" << i << ":";
		
		if (K >= C) {
			for (j = 0; j < K; j++) {
				position = position + j*pow(K, C-1-groupNum);
				groupNum++;
				if (groupNum == C) {
					cout << " " << position + 1;
					if (find(vp.begin(), vp.end(), position) != vp.end()) {
						cout << "something very very wrong " << i << endl;
					}
					vp.push_back(position);
					
					if (position > maxNum) {
						cout << " something is wrong" << endl;
					}
					
					groupNum = 0;
					position = 0;
				}
			}
			
			if (K%C != 0) {
				cout << " " << position + 1;
				if (find(vp.begin(), vp.end(), position) != vp.end()) {
					cout << "something very very wrong " << i << endl;
				}
				vp.push_back(position);
				if (position > maxNum) {
					cout << " something is wrong" << endl;
				}
			}
		} else {
			for (j = 0; j < K; j++) {
				position = position + j*pow(K, K-1-j);	
			}
			
			for (j=0;j<C-K;j++){
				position = position*K;
			}
			
			cout << " " << position+1;
			if (find(vp.begin(), vp.end(), position) != vp.end()) {
				cout << "something very very wrong " << i << endl;
			}
			vp.push_back(position);
			if (position > maxNum) {
				cout << " something is wrong" << endl;
			}
		}
		
		cout << endl;
		
		if (numPts != vp.size()) {
			cout << "something very wrong " << i << endl;
		}
		
		/*
		for (j=0;j<K;j++) {
			s = makeString (K, j+1);
			//cout << "string " << s << endl;
			s = makeBigString(s, C, K);
			//cout << "bigstring " << s << endl;
			flag = 0;
			//cout << "dbg1 " << vp.size() << " " << vp[0] << " " << s[0] << endl;
			for (k = 0; k < vp.size(); k++) {
				if (s[vp[k]] == 'G') {
					flag = 1;
					break;
				}
			}
			
			if (flag == 0) {
				cout << "check something wrong here " << i << endl;
			}
		}*/
	}
	
	return 0;
}

string makeString (int l, int p) {
	string s = "";
	int i;
	for (i=0;i<l;i++) {
		if (i != p-1) {
			s = s + 'L';
		} else {
			s = s + 'G';
		}
	}
	
	return s;
}

string makeBigString (string original, int times, int size) {
	string s = original;
	string temp = "";
	string Gstring = "";
	int i;
	
	for (i=0;i<size;i++) {
		Gstring = Gstring + 'G';
	}
	
	unsigned long long int actSize = size;
	unsigned long long int j;
	
	for (i=1;i<times;i++) {
		temp = "";
		for (j=0;j<actSize;j++) {
			if (s[j] == 'L') {
				temp = temp + original;
			} else {
				temp = temp + Gstring;
			}
		}
		s = temp;
		actSize = actSize*size;
		//cout << "done times " << i << " size " << actSize << endl;
	}
	
	return s;
}

