#include <iostream>
#include <deque>
#include <cstring>
#include <stdio.h>
//#include <algorithm>

using namespace std;

int main() {
	FILE *fp = fopen("input.in", "r");
	if (!fp) {
		cout << "Cant open file" << endl;
		return 0;
	}

	int nTests = 0;
	fscanf(fp, "%d", &nTests);

	for (int i = 0; i < nTests; ++i) {

		char input[16] = {'\0'};
		fscanf(fp, "%s", input);

		int len = strlen(input);

		deque<char> dq;
		dq.push_front(input[0]);
		for (int j = 1; j < len; ++j) {
			if (input[j] >= dq.front()) {
				dq.push_front(input[j]);
			}
			else {
				dq.push_back(input[j]);
			}
		}

		cout<< "Case #" << i + 1 << ": ";
		deque<char>::iterator it = dq.begin();
		for (; it != dq.end(); ++it) {
			cout<<*it;
		}
		cout<<endl;
	}
	return 0;
}
