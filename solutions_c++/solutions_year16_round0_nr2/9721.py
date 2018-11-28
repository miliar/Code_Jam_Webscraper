#include <iostream>
#include <string>

using namespace std;

int main()
{
	string s;
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i){
		cin >> s;
		string reduced;
		int len = s.length(), j = 0;
		while(j != len) {
			char c = s[j];
			++j;
			while((j != len) && (s[j] == c))
				++j;
			reduced += c; 
		}
		len = reduced.length();
		int ans = 0;
		for(int j = 0; j < len; ++j) {
			if(reduced[j] == '-') {
				if(j == 0)
					++ans;
				else
					ans += 2;
			}
		}
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}