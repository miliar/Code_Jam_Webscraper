#include "iostream"
#include "stdio.h"
#include "vector"
#include "queue"
#include "algorithm"
#define MAXN 100005
using namespace std;

char reverse(char a) {
	if (a=='+') return '-';
	else return '+';
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin >> T;
	for (int cst = 1; cst <= T; cst++) {
		cout << "Case #" << cst << ": ";
		string str;
		cin >> str;
		int ans = 0;
		int last = str.length();
		while(true) {
			while (last > 0 && str[last-1] == '+') {
				last--;
			}
			if (last == 0) break;
			ans++;
			// cout << str << endl;
			if (str[0] == '+') {
				int last2 = last;
				while (last2 > 0 && str[last2-1] == '-') {
					last2--;
				}
				for (int i = 0; i < last2; i++) {
					char tmp = str[i];
					str[i] = reverse(str[last2-1]);
					str[last2-1] = reverse(tmp);
					last2--;
				}
			}
			else {
				int last2 = last;
				while (last2 > 0 && str[last2-1] == '+') {
					last2--;
				}
				for (int i = 0; i < last2; i++) {
					char tmp = str[i];
					str[i] = reverse(str[last2-1]);
					str[last2-1] = reverse(tmp);
					last2--;
				}
			}
		}
		cout << ans << endl;
	}	
}