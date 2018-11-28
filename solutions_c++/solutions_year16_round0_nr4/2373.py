#include<iostream>
#include<fstream>
#include<vector>
#include<sstream>
using namespace std;
string increaseDivisor(string& str, int base,int& upper) {
	int len = str.length();
	int index = len - 1;
	while (index >= 0 && upper == 1) {
		if (str[index] - '0'<base - 1) {
			upper = 0;
			str[index]++;
			break;
		}
		else {
			str[index] = '0';
			upper = 1;
		}
		index--;
	}
	return string(str);
}
string genComplexity(string& origin, int c) {
	string str(origin);
	int originLen = origin.length();
	for (int i = 1; i < c; i++) {
		ostringstream ostr;
		int len = str.length();
		for (int j = 0; j < len; j++) {
			if (str[j] == '0') {
				for (int k = 0; k < originLen; k++) {
					ostr << '0';
				}
			}
			else {
				for (int k = 0; k < originLen; k++)
					ostr << origin[k];
			}
		}
		str = ostr.str();
	}
	return str;
}
int main() {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int caseCount = 0;
	scanf("%d", &caseCount);
	for (int i = 0; i < caseCount; i++) {
		int K = 0, C = 0, S = 0;
		scanf("%d %d %d", &K, &C, &S);
		long long partSize = 1;
		for (int j = 0; j < C - 1; j++)
			partSize *= K;
		cout << "Case #" << i + 1<<":";
		if (partSize < 1)cout << "IMPOSSIBLE";
		else if (C == 1) {
			if(S<K)
				cout << " IMPOSSIBLE";
			else {
				for (int j = 0; j < K; j++) {
					cout <<" "<< j + 1;
				}
			}
		}
		else if (C >= 2 && S < K / 2)
			cout << " IMPOSSIBLE";
		else {
			long long index = 1;
			long long limit = pow(K, C);
			for (int j = 0; j < K; j++) {
				cout << " " << index;
				index += partSize;
			}
		}
		cout << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}