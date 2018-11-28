#include <iostream>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		int end = -1;
		for(int j = s.length() - 1; j >= 0; j--) {
			if(s[j] == '-') {
				end = j;
				break;
			}
		}
		//cout << "here" << endl;
		int cnt = 0;
		while(end >= 0) {
			if(s[0] != '-') {
				int e = 0;
				for(int j = 0; j < s.length() && j <= end; j++) {
					if(s[j] == '-')
						break;
					e++;
				}
				string s2 = s.substr(0,e);
				reverse(s2.begin(), s2.end());
				for(int j = 0; j < e; j++)
					s[j] = s2[j] == '-' ? '+' : '-';
			} else {
				string s2 = s.substr(0,end+1);
				reverse(s2.begin(), s2.end());
				for(int j = 0; j <= end; j++)
					s[j] = s2[j] == '-' ? '+' : '-';
			}
			//cout << i << " " << end << " " << s << endl;
			cnt++;
			end = -1;
			for(int j = s.length() - 1; j >= 0; j--) {
				if(s[j] == '-') {
					end = j;
					break;
				}
			}
		}
		printf("Case #%d: %d\n", i,cnt);
	}
}