#include <bits/stdc++.h>
#define endl "\n"

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	
	int n;
	cin >> n;
	cin.ignore();

	for(int i = 0; i < n; i++) {
		string line;
		getline (cin, line);
		int changes = 1;
		for(int j = 1; j < line.size(); j++) {
			if(line[j-1] != line[j]) changes++;
		}
		if(line[line.size()-1] == '+') changes--;
		cout << "Case #" << (i+1) << ": " << changes << endl;
	}

	return 0;
}
