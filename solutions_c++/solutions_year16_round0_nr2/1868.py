#include<iostream>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output-large.txt", "w", stdout);
	int n;
	cin >> n;
	
	
	
	for(int i = 1; i <= n; i++) {
		string line;
		cin >> line;
		if(line == "") {
			cout << "Case #" << i << ": 0" << endl;
			continue;
		}
		line += '+';
		
		int changes = 0;
		for(int j = 0 ; j < line.length()-1; j++) {
			if(line[j] != line[j+1]) {
				changes++;
			}
		}
		cout << "Case #" << i << ": " << changes << endl;
	}
	return 0;
}