#include <iostream>
#include <cstring>

using namespace std;

int main() {
	int T;
	char S[101];
	int len, count;
	char last, curr;
	char* pcurr;

	cin >> T;
	for(int t=0; t<T; t++) {
		cin >> S;
		len = strlen(S);
		last = 0;
		count = 0;

		for(pcurr=S; *pcurr!='\0'; pcurr++) {
			curr = *pcurr;
			if(curr != last && curr == '-')
				count++;
			last = curr;
		}

		cout << "Case #" << (t+1) << ": " << (count * 2 - ((S[0] == '-') ? 1 : 0)) << endl;
	}

	return 0;
}
