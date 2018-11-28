#include <string>
#include <cstdio>
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <stack>
#include <fstream>

using namespace std;

#define PQ priority_queue
typedef long long LL;
typedef pair<LL,LL> pll;

int main() {
	ifstream F;
	F.open ("A-large.in");
	ofstream O;
	O.open ("A_out.txt");

	int T;
	string S1,S2;
	F >> T;
	getline(F,S1);
	for (int i=1;i<=T;i++) {
		getline(F,S1);
		S2 = "";
		for (int j=0;j<S1.length();j++) {
			if (j==0) {
				S2 += S1[j];
				continue;
			}
			bool found = false;
			for (int k=0;k<S2.length();k++) {
				if (S2[k]<S1[j]) {
					string tmp;
					tmp += S1[j];
					S2 = tmp+S2;
					found = true;
					break;
				}
				else if (S2[k]>S1[j]) {
					S2 += S1[j];
					found = true;
					break;
				}
			}
			if (!found) S2+= S1[j];
		}
		O << "Case #" << i << ": " << S2 << endl;
	}
	return 0;
}
