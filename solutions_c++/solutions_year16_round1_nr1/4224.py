#include <iostream>
#include <algorithm>

using namespace std;
string process(string s) {
	string ret = "";
	ret += s[0];
	for (int i = 1; i < s.length(); i++) {
		if (s[i] < ret[0]) {
			ret = ret + s[i];
		} else {
			ret = s[i] + ret;
		}
	}
	return ret;
}
int main() {
	int N;
	scanf("%d", &N);
	int cases = 0;
	while (N--) {
		cases++;
		string s;
		cin >> s;
		printf("Case #%d: ", cases);
		string ret = process(s);
		cout << ret << endl;
	}
}