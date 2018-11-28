#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <iomanip>

using namespace std;

int main(){
	ifstream inData("small.in");
	ofstream outData("output-small.txt");
	int num;
	inData >> num;
	for(int i = 0; i < num; i++){
		int t;
		inData >> t;
		string p;
		inData >> p;
		int n = 0;
		int sum = 0;
		cout << p << endl;
		for (int j = 0; j <= t; j++) {
			if (j > sum && atoi((p.substr(j,1)).c_str()) != 0) {
				n += j-sum;
				sum += n;
			} 
			cout << "sum: " << sum << " ppl: " << p[j] << endl;
			sum += atoi((p.substr(j,1)).c_str());
		}
		outData << "Case #" << i+1 << ": " << n << endl;
	}

	return 0;
}