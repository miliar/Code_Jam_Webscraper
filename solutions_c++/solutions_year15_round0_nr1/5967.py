#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cstdlib>
using namespace std;


int main() {
	// your code goes here

	int nCases; cin >> nCases;
	for(int caseNum=1; caseNum<=nCases;caseNum++) {
		int maxShyness; string s;cin >> maxShyness >> s;
		vector<int>shyArray;
		for(int i=0;i<s.size();i++) {
			int v = atoi((string("")+s[i]).c_str());
			shyArray.push_back(v);
		}
		
		int tot=0;
		int nAdded = 0;
		for (int i=0;i<shyArray.size();i++) {
			if (shyArray[i]) {
				if (tot + nAdded < i) {
					nAdded+=i-(tot+nAdded);
				} 
				tot+=shyArray[i];
			}
		}
		
		cout << "Case #" << caseNum << ": " << nAdded << endl;
		
	}
	return 0;
}