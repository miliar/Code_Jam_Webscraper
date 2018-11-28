#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t, m = 1, i, j;
	cin >> t;
	while(t--) {
		char str[101], str2[101];
		cin >> str;
		i = j = 1;
		cout << "Case #" << m++ << ": ";
		str2[0] = str[0];
		while(str[i] != '\0') {
			if(str[i] != str2[j-1]) {
				str2[j++] = str[i];
			}
			i++;
		}
		str2[j] = '\0';
		if(str2[j-1] == '+') {
			cout << j-1 << endl;
		}
		else {
			cout << j << endl;
		}
	}
	return 0;
}
