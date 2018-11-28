#include <iostream>
#include <vector>
#include <string>
using namespace std;

//true = +, false = -

int upper(vector<bool> cookies) {
	int nbCoups = 0;
	bool orientation = cookies[0];
	for (int iCookie = 0; iCookie < cookies.size(); iCookie++) {
		if (cookies[iCookie] != orientation) {
			orientation = cookies[iCookie];
			nbCoups++;
		}
	}
	if (orientation == false)
		nbCoups++;
	return nbCoups;
}

int main(void) {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		string s;
		vector<bool> b;
		cin >> s;
		for (int k = 0; k < s.length(); k++) {
			if (s[k] == '+')
				b.push_back(true);
			else if (s[k] == '-')
				b.push_back(false);
		}
		printf("Case #%d: %d\n", i+1, upper(b));
	}
	return 0;
}
