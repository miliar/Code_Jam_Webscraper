#include <stdio.h>
#include <set>

using namespace std;

int main() {

	FILE* in = fopen("A-large.in", "rb");
	FILE* out = fopen("A-large_out.txt", "wb");

	int n = 0;
	fscanf(in, "%d", &n);

	for(int i = 1; i <= n; ++ i) {
		int a = 0;
		fscanf(in, "%d", &a);

		if(a == 0) {
			fprintf(out, "Case #%d: INSOMNIA\n", i);
			continue;
		}

		int num = 0;

		set<int> dig; 
		while(dig.size() < 10) {
			num += a;

			int b = num;

			while(b > 0) {
				dig.insert(b % 10);
				b /= 10;
			}
		}

		fprintf(out, "Case #%d: %d\n", i, num);
	}

	return 0;
}