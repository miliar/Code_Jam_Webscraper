#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAX_S = 111;

char instance[MAX_S];
int len;
bool bitArray[MAX_S];

void toBitArray() {
	for (int i = 0; i < len; i++)
		if (instance[i] == '+') bitArray[i] = 1;
}

int getLIndex(int RIndex) {
	if (!bitArray[0]) return -1;

	int LIndex = 0;
	for (int i = 1; i < RIndex; i++) {
		if (!bitArray[i]) break;
		else LIndex = i;
	}

	return LIndex;
}

void operation(int index) {
	for (int i = 0; i <= index; i++) bitArray[i] ^= 1;
	reverse(bitArray, bitArray + index + 1);
}

int main() {

	int testcase;
	scanf("%d", &testcase);

	for (int tc = 1; tc <= testcase; tc++) {
		memset(bitArray, 0, sizeof(bitArray));

		int cnt = 0;
		scanf("%s", instance);
		len = strlen(instance);

		toBitArray();

		int LIndex, RIndex;
		for (RIndex = len - 1; RIndex >= 0; RIndex--) {
			if (!bitArray[RIndex]) {
				LIndex = getLIndex(RIndex);

				if(0 <= LIndex) operation(LIndex), cnt++;
				
				operation(RIndex);
				cnt++;
			}
		}
		
		printf("Case #%d: %d\n", tc, cnt);
	}

	return 0;
}