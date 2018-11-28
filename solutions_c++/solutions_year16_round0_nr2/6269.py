#include<cstdio>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
int main() {
	int n, kase = 0; cin >> n; char s[105];
	while (n--) {
		scanf("%s",s);
		int id=0,ans=0;
		do {
			id=0;
			for (int i = strlen(s) - 1; i >= 0; i--) {
				if (s[i] == '-') { id = i+1; break; }
			}
			
			if (id > 0) {
				ans++;
				for (int i = 0; i < id; i++) {
					if (s[i] == '-') s[i] = '+';
					else s[i] = '-';
				}
			}
		} while (id != 0);
		printf("Case #%d: %d\n",++kase,ans);
	}
	//system("PAUSE");
	return 0;
}