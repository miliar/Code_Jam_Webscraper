#include <iostream>
#include <algorithm>
#include <fstream>
#include <string>
int o = 0;
using namespace std;
int main(){
	string s;
	ifstream cin ("B-large.in");
	ofstream cout ("output.out");
	int t;
	cin >> t;

	while (t--){
		o++;
		cin >> s;
		int ans = 0;
		for (int i = 0; i < s.size() - 1; i++)
			if (s[i] != s[i + 1])
				ans++;
		if (s[s.size() - 1] == '-')
			ans++;
		cout << "Case #" << o << ": " << ans << endl;
	}

	return 0;
}