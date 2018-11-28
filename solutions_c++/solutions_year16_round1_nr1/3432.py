#pragma warning(disable:4996) 

#include <cstdio>
#include <deque>

using namespace std;

const int length = 1001;

int main(void) {
	FILE * fp;
	fp = fopen("A.txt", "w");
	int n;
	scanf("%d", &n);
	
	for (int k = 1; k <= n; k++) {
		char s[length];
		scanf("%s", &s);

		deque<char> v;

		v.push_back(*(s));
		for (int i = 1; i < strlen(s); i++) {
			if (v.front() > *(s + i)) {
				v.push_back(*(s + i));
			}
			else {
				v.push_front(*(s + i));
			}
		}

		fprintf(fp, "Case #%d: ", k);
		for (int i = 0; i < v.size(); i++) {
			fprintf(fp, "%c", v[i]);
		}
		fprintf(fp, "\n");
	}
	return 0;
}