#include <string.h>
#include <iostream>
#include <vector>
using namespace std;

vector<int> GetSolution(char*);

int main(void) {
	int t;
	char in[2001];
	vector<int> oResult;
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

vector<int> GetSolution(char* in) {
	vector<int> oRet;

	const char* arrSpell[10] = {
		"ZERO",
		"ONE",
		"TWO",
		"THREE",
		"FOUR",
		"FIVE",
		"SIX",
		"SEVEN",
		"EIGHT",
		"NINE",
	};

	vector<int> vecTestCase[10];
	for (int i=0; i<10; i++) {
		vecTestCase[i].resize(26);
		const char* szSpell = arrSpell[i];
		int nLength = strlen(szSpell);
		for (int j=0; j<nLength; j++) {
			char nSpell = szSpell[j];
			vecTestCase[i][nSpell - 'A']++;
		}
	}

	vector<int> vecInput;
	vecInput.resize(26);
	for (int i=0; i<strlen(in); i++) {
		char nSpell = in[i];
		vecInput[nSpell - 'A']++;
	}

	vector<int> vecStack;
	vector<int> vecData = vecInput;
	int idx = 0;
	//cout << endl;
	//cout << "[" << in << "] -> "; for (int k=0; k<vecData.size(); k++) cout<< vecData[k]; cout<< endl;
	while(true) {
		bool bSucceed = true;
		//cout << "TRY [" << idx << "] : ";
		for (int i=0; i<26; i++) {
			int diff = vecData[i] - vecTestCase[idx][i];
			//cout << diff;
			if (diff < 0) {
				bSucceed = false;
				break;
			}
		}
		//cout << endl;
		if (bSucceed) {
			int sum = 0;
			for (int i=0; i<26; i++) {
				vecData[i] -= vecTestCase[idx][i];
				sum += vecData[i];
			}
			vecStack.push_back(idx);
			//cout << "STATUS D : "; for (int k=0; k<vecData.size(); k++) //cout<< vecData[k]; cout<< endl;
	   		//cout << "STATUS S : "; for (int k=0; k<vecStack.size(); k++) cout<< vecStack[k]; cout<< endl;
			if (sum == 0) {
				break;
			}
		} else {
			if (++idx > 9) {
				if (!vecStack.empty()) {
					idx = vecStack.back() + 1;
					vecStack.pop_back();
					for (int i=0; i<26; i++) {
						vecData[i] += vecTestCase[idx-1][i];
					}
					//cout << "STATUS D : "; for (int k=0; k<vecData.size(); k++) cout<< vecData[k]; cout<< endl;
			   		//cout << "STATUS S : "; for (int k=0; k<vecStack.size(); k++) cout<< vecStack[k]; cout<< endl;

				} else {
					//cout << "Error!" << endl;
					break;
				}
			}
		}
	}

	oRet = vecStack;
	
	return oRet;
}
