#include <bits/stdc++.h>
using namespace std;

#define ARRAY_LEN(array) (sizeof(array) / sizeof(*array))
#define SIZEOF_MEMBER(type, member) (sizeof(((type *) NULL)->member))

typedef int64_t Num;
const char *PRINUM = PRId64;
const char *SCANUM = SCNd64;

void handle_case(int case_num) {
	char line[2048];
	fgets(line, sizeof(line), stdin);

	string result = "";
	result.reserve(strlen(line));
	for (int i = 0; i < strlen(line); i++) {
		if (line[i] < 'A' || line[i] > 'Z')
			continue;
		if (line[i] >= result[0]) {
			result.insert(0, 1, line[i]);
		} else {
			result.push_back(line[i]);
		}
	}

	fputs(result.c_str(), stdout);
}

int main(void) {
	char n_cases_str[64];
	fgets(n_cases_str, sizeof(n_cases_str), stdin);
	int n_cases;
	sscanf(n_cases_str, " %d ", &n_cases);

	for (int case_num = 1; case_num <= n_cases; case_num++) {
		printf("Case #%d: ", case_num);
		handle_case(case_num);
		printf("\n");
	}

	return 0;
}
