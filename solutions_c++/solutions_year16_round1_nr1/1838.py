#include <iostream>
#include <cstdio>
using namespace std;

int main () {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int T;
	string str;
	string mejor[1024];
	
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> str;
		mejor[0] = str[0];
		
		string aux1, aux2;
		for (int i = 1; i < (int) str.size(); i++) {
			aux1 = mejor[i-1] + str[i];
			aux2 = str[i] + mejor[i-1];
			if (aux1 < aux2)
				mejor[i] = aux2;
			else
				mejor[i] = aux1;
		}
	
		cout << "Case #" << t << ": " << mejor[(int) str.size() - 1] << endl;
	}
}
