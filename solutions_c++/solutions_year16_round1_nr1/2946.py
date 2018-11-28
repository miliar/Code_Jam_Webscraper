#include <iostream>
#include <unordered_map>
#include <list>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

int main() {
	
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		string s;
		cin >> s;
		string s2 = "";
		for (int j = 0; j < s.size(); ++j) {
			if (s[j] >= s2[0]) s2 = s[j] + s2;
			else s2 = s2 + s[j]; 
		}
		cout << "Case #"<< i + 1<< ": "; 
		cout << s2 << endl;
	}
}
