#include <iostream>
#include <fstream>
#include <string>
using namespace std;
          
int main() {

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;
	for(int i = 0; i < T; i++) {
		string s;
		int cnt = 0;
		cin >> s; 
		for (int i = 1; i < s.size(); i++) {
			if (s[i] != s[i - 1])
				cnt++;
		} 
		if(s[s.size() - 1] == '-')
			cnt++;
		cout << "Case #" << i + 1 << ": " << cnt << endl;
	}
	return 0;
}