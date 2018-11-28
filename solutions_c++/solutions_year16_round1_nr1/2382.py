#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("large-output.out", "w", stdout);
	int n;
	cin >> n;
	int i = 1;
	while(i <= n) {
		string line;
		cin >> line;
		string result = "";
		result += line[0];
		for(int j = 1; j <= line.length()-1; j++) {
			if((int)line[j] >= (int)result[0]) {
				result = line[j] + result;
			} else {
				result = result + line[j];
			}
		}
		i++;
		cout << "Case #" << i-1 << ": " << result << endl;
	}
	
	return 0;
}