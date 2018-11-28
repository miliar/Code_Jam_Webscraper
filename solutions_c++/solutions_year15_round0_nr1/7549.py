#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int n = 0;
		int S;
		string str;
		
		int tot = 0;
		cin >> S >> str;
		for (int i = 0; i <= S; i++) {
			int v = str[i] - '0';
			if (tot < i) {
				n += (i - tot);
				tot += (i - tot);
			}
			tot += v;
		}
		cout <<"Case #"<< t <<": "<< n << endl;
	}
}