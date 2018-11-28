#include <stdio.h>
#include <string.h>
#include <set>

using namespace std;

int main() {

	FILE* in = fopen("B-large.in", "rb");
	FILE* out = fopen("B-large_out.txt", "wb");

	int n = 0;
	fscanf(in, "%d", &n);

	for(int i = 1; i <= n; ++ i) {
		char c;

		bool positive = true;
		int res = 0;

		char line[200];
		fscanf(in, "%s", line);

		for(int count = 0, len = strlen(line); count < len; ++ count) {
			c = line[count];
			if(c == '-') {
				if(positive) {
					positive = false;

					res += ((count > 0)?2:1);
				}
			} else {
				positive = true;
			}
		} 

		fprintf(out, "Case #%d: %d\n", i, res);
	}

	return 0;
}