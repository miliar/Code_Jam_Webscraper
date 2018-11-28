#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>
#include <string.h>

using namespace std;

int main() {
	int n;
	string line;

	cin >> n;
	getline(cin, line);

	for (int i = 0; i < n; i++) {
		map<int, char> m;
		int b = 0, e = 0;
		getline(cin, line);
	
		m[b] = line[0];
		for (int j = 1; j < line.length(); j++){
			if (line[j] >= m[b]) {
				b--;
				m[b] = line[j];
			} else {
				e++;
				m[e] = line[j];
			}
		}

		cout << "Case #" << i + 1 << ": ";

		for (auto it = m.begin(); it != m.end(); it++)
			cout << it->second;
		cout << endl;
	}

	return 0;
}

