#include <string>
#include <iostream>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		string s;
		cin>>s;
		string ans = "";
		ans += s[0];
		for (int i=1; i < s.size(); i++) {
			string ans1 = ans + s[i];
			string ans2 = s[i] + ans;
			ans = ans1 < ans2 ? ans2 : ans1;
		}
		printf("Case #%d: ", t);
		cout << ans << endl;
	}
	return 0;
}
