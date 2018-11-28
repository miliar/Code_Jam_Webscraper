#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main() {
	int testNum;
	cin >> testNum;
	int caseNum = 0;

	while (++caseNum <= testNum) {
		int Smax, standing = 0, need = 0;
		cin >> Smax;
		string list;
		cin >> list;

		for (int shy=0; shy <= Smax; ++shy) {
			if (standing >= shy)
				standing += list[shy] - '0';
			else {
				need += shy - standing;
				standing = shy + list[shy] - '0';
			}
		}

		printf("Case #%d: %d\n", caseNum, need);
	}
	return 0;
}

