// not sure :P

#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

void test_case(int t) {
	char str[100];
	cin >> str;
	int l = strlen(str);
	
	int res = 0;
	int i = l-1;
	while (i>=0 && str[i] == '+') i--;
	while (i >= 0) {
		if (i == l || str[i] != str[i+1])
			res++;
		i--;
	}
	
	cout << "Case #" << t << ": " << res << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t=1; t <= T; t++)
		test_case(t);
	
	return 0;
}
