#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cctype>
using namespace std;

int T;
int a, b, k;

int main() {
	cin >> T;
	for (int cc = 1; cc <= T; cc++) {
		printf("Case #%d: ", cc);

		cin >> a >> b >> k;
		int count = 0;
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				if ((i & j) < k)
					count++;
			}
		}
		cout << count << endl;
	}



	return 0;
}