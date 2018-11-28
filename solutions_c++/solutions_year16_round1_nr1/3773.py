#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	string s;

	scanf("%d", &t);
	int count = 1;
	while(t--){
		cin >> s;
		vector<char> resp;
		resp.push_back(s[0]);
		for(int i = 1; i < s.size(); i++){
			if(s[i] >= resp[0]) {
				resp.insert(resp.begin(), s[i]);
			} else {
				resp.push_back(s[i]);
			}
		}
		printf("Case #%d: ", count++);
		for (int i = 0; i < resp.size(); i++) {
			printf("%c", resp[i]);
		}
		printf("\n");
	}
	return 0;
}