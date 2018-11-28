#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <vector>
using namespace std;
enum foo {
	PLUS = 1, MINUS = -1,
};
void flip(vector<unsigned char> &vec)
{
	for(auto it = vec.begin(); it != vec.end(); ++it) {
		*it = -(*it);
	}
}
int dothis(vector<unsigned char> &vec, int len)
{
	if (vec.size() == 0)
		return len;
	while (vec.back() == PLUS)
		vec.pop_back();
	if (vec.size() == 0)
		return len;
	flip(vec);
	return dothis(vec, 1+len);
}
int main (int argc, char **argv) {
	FILE *fp = fopen(argv[1], "r");
	int i, num, max;
	fscanf(fp, "%d\n", &max);
	for(i=1;i<=max;i++) {
		vector <unsigned char> list;
		char next='?',last='?';
		while (next != '\n') {
			fscanf(fp, "%c", &next);
			if (next == last)
				continue;
			if (next == '-')
				list.push_back(MINUS);
			if (next == '+')
				list.push_back(PLUS);
			last = next;
		}
		printf("Case #%d: %d\n", i, dothis(list, 0));
	}
}
