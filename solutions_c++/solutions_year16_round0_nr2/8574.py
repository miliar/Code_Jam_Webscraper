#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
char s[105];

void change(char &c) {
	if(c == '-')
		c = '+';
	else c = '-';
}

int main() {
	int T, counter; char last; scanf("%d", &T);
	for(int TT = 1; TT <= T; ++TT) {
		printf("Case #%d: ", TT);
		scanf("%s", s);
		int n = strlen(s);
		counter = 0, last = s[0];
		for(int i = 1; i < n; ++i)
			if(s[i] != last) {
				change(last);
				counter++;
			}
		if(s[n-1] == '-') counter++;
		cout << counter << endl;
	}
	return 0;
}
