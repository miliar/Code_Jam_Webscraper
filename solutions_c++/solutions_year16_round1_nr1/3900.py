#include <iostream>
#include <bitset>
#include<math.h>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
#include <fstream>
using namespace std;


string
processWrd(string hWrd) {

	string ans, temp;
	

		
	for (int i = 0; i < hWrd.length(); i++) {
		if (ans.empty()) {
			ans.append(1, hWrd[i]);
		}
		else {
			if (hWrd[i] >= ans[0]) {
				temp = hWrd[i];
				temp.append(ans);
				ans = temp;
			}
			else {
				ans.append(1, hWrd[i]);
			}
		}
	}

	return ans;
}

int main() {

	int testNum;
	string hostWrd;
	string finalWrd;
	unsigned long long startVal = 0, endVal;
	ofstream outFileStream;
	outFileStream.open("output.txt");

	cin >> testNum;

	for (int i = 1; i <= testNum; i++) {
		cout << "Case #" << i << ":" << " ";
		outFileStream << "Case #" << i << ":" << " ";
		cin >> hostWrd;
		finalWrd = processWrd(hostWrd);
		cout<< finalWrd << endl;
		outFileStream << finalWrd << endl;
	}
}