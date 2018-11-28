#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;
    std::cin.get();
    for (int kase = 1; kase <= t; ++kase) {
		string a;
        std::getline (std::cin, a);
		int ans = 1;
		char curr = a[0];
		for (int i = 1; i < a.length(); ++i) {
			if (a[i] == curr) {
				continue;
			} else {
				ans++;
				curr = a[i];
			}
		}
		if(curr == '+') {
			ans--;
		}
		printf("Case #%d: %d\n", kase, ans);
    }
    return 0;
}