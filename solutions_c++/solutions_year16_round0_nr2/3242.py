#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;

int main() {
	ios::sync_with_stdio();

	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; tt++) {
		string input ;
		cin >> input;
		char arr[input.length() + 1] ;
		strcpy(arr, input.c_str());
		int values[input.length() + 1];
		memset(values, 0, sizeof values);
		if (arr[0] == '-')
			values[0] = 1;
		for (int i = 1; i < input.length(); i++) {
			if (arr[i] == '-') {
				if (arr[i - 1] == '+') {
					// if (values[i - 1] == 0) {
						values[i] = values[i - 1]+2;
					// } else {
					// 	values[i] = values[i - 1] + 1;
					// }
				} else {
					values[i] = values[i - 1];
				}
			}else{
				values[i] = values[i - 1];
			}
		}
		printf("Case #%d: ",tt);
		cout << values[input.length() - 1] << endl;
	}
}