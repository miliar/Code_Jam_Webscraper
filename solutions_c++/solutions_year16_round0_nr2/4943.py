#include <cstdio>
#include <cstring>
#include <cassert>
#include <vector>
#include <algorithm>
using namespace std;
const int MAX_BUFF = 110;

int testCases;
char buff[MAX_BUFF], inp[MAX_BUFF];

int main() {
	sscanf(gets(buff), "%d", &testCases);
	for(int t = 1; t <= testCases; t++) {
		sscanf(gets(buff), "%s", inp);
		int len = strlen(inp);
		char last_sign = inp[0];
		int num_flips = 0;
		for(int i = 1; i < len; i++) {
			if(inp[i] != last_sign) {
				last_sign = inp[i];
				num_flips++;
			}
		}
		if(last_sign == '-') num_flips++;
		printf("Case #%d: %d\n", t, num_flips);		
	}
	return 0;
}