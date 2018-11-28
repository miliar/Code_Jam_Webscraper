#include <string.h>
#include <iostream>
#include <deque>
using namespace std;

deque<char> GetSolution(char*);

int main(void) {
	int t;
	char in[1001];
	deque<char> oResult;
	cin >> t; 
	for (int i = 1; i <= t; ++i) {
		cin >> in;

		oResult = GetSolution(in);

		cout << "Case #" << i << ": ";
		for (int j=0; j<oResult.size(); j++) cout << oResult[j];
		cout << endl;
	}

	return 0;
}

deque<char> GetSolution(char* in) {
	deque<char> oRet;	
	int nLength = strlen(in);
	for (int i=0; i<nLength; i++) {
		if (oRet.empty()) {			
			oRet.push_back(in[i]);
		} else {
			if (in[i] >= oRet[0]) {
				oRet.push_front(in[i]);
			} else {
				oRet.push_back(in[i]);
			}
		}
		//for (int j=0; j<oRet.size(); j++) cout << oRet[j];
	}
	return oRet;
}
