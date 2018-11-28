#include <stdio.h>
#include <cstring>
#include <iostream>
#include <bitset>
using namespace std;

static int g_flipCount = 0;
void flip(bitset<100> &set, int pos) {
	bool flip = false;
	int start = 0;
	int end = pos;
	//swap
	while (start < end) {
		bool temp = set[start];
		set[start] = set[end];
		set[end] = temp;
		++start;
		--end;
	}
	// toggle
	start = 0;
	while (start <= pos) {
		if (!flip) {
			flip = true;
			++g_flipCount;
		}
		set.flip(start);
		++start;
	}

}

void arrange(bitset<100> &set, int size) {
	int flipPos = -1;
	int i = size - 1;
	while (i >= 0) {
		if (!set[i]) {
			flipPos = i;
			break;
		}
		--i;
	}

	if (flipPos != -1) {
		int j = 0;
		int flipPos2 = -1;
		while (j <= flipPos) {
			if (!set[j]) {
				flipPos2 = j - 1;
				break;
			}
			++j;
		}
		if (flipPos2 != -1) flip(set, flipPos2);
		flip(set, flipPos);
		arrange(set, flipPos);
	}
}

int main() {

	FILE *fp = fopen("input.in", "r");
	if (!fp) {
		cout << "Cant open file" << endl;
		return 0;
	}

	int nTests = 0;
	fscanf(fp, "%d", &nTests);

	for (int i = 0; i < nTests; ++i) {
		char str[101] = {'\0'};
		fscanf(fp, "%s", str);

		int len = strlen(str);
		bitset<100> set;

		for (int j = 0; j < len; ++j) {
			if (str[j] == '+') set.set(j, true);
		}

		g_flipCount = 0;
		arrange(set, len);

		cout << "Case #" << i + 1 << ": " << g_flipCount << endl;
	}
	return 0;
}

