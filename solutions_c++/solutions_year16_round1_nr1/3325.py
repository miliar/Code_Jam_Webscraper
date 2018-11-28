#include <cstdio>
#include <cstring>
#include <deque>

using namespace std;

int main() {
	int testcases;
	int slen;
	char mystr[1005];

	deque <char> laststr;

	scanf("%d", &testcases);

	for(int t = 1; t <= testcases; ++t) {
		scanf("%s", mystr);

		slen = strlen(mystr);

		laststr.push_back(mystr[0]);

		for(int i = 1; i < slen; ++i) {
			char frontlett = laststr.front();
			char backlett = laststr.back();

			if(mystr[i] >= frontlett) {
				laststr.push_front(mystr[i]);
			}
			else {
				laststr.push_back(mystr[i]);
			}
		}

		printf("Case #%d: ", t);
		while(!laststr.empty()) {
			printf("%c", laststr.front());

			laststr.pop_front();
		}
		printf("\n");
	}

	return 0;
}