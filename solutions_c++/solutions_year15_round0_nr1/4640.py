#include <iostream>

using namespace std;
int main(){
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int t,sm,l,min,st;
	char s[1001];
	cin >> t;
	for (int cases = 0; cases < t; cases++){
		
		cin >> sm;
		cin >> s;
		l = strlen(s);
		st = 0;
		min = 0;
		for (int i = 0; i < l; i++){
			if (i<=st) 	st += s[i] - 48;
			else {
				min += i - st;
				st += i - st;
				st += s[i] - 48;
			}

		}
		cout << "Case #" << cases+1 << ": " << min << endl;
	}
	return 0;
}