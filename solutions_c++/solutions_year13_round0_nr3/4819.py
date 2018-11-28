#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

FILE *input;
FILE *output;
char buff[1024];

#define DEBUG 0

#define FETCH_E do {\
	memset(buff, 0, 1024);\
	fgets(buff, 1024, input);\
	if (DEBUG) \
		printf("%s\n", buff);\
	} while(0)

vector<long> _cache;

void AddToCache(long val);
bool CheckPalindrome(long val);

int main(int argC, char *argV[]) {
	char *fileIn = argV[1];

	input = fopen(argV[1], "r");
	output = fopen("C.out", "w");
	
	int cases;
	FETCH_E;
	sscanf(buff, "%d", &cases);

	for (int c = 0; c < cases; c++) {
		FETCH_E;
		int low, high;
		sscanf(buff, "%d %d", &low, &high);
		int count = 0;
		int low_r = (int) sqrt((double) low);
		int high_r = (int) sqrt((double) high);
		if (low_r * low_r != low)
			low_r++;

		for (int i = low_r; i <= high_r; i++) {
			if (CheckPalindrome(i) && CheckPalindrome(i * i))
				count++;
		}
		fprintf(output, "Case #%d: %d\n", c + 1, count);
	}

	fclose(input);
	fclose(output);

	return 0;
}

void AddToCache(long val) {
	_cache.push_back(val);
	sort(_cache.begin(), _cache.end());
}

bool CheckPalindrome(long val) {
	if (binary_search(_cache.begin(), _cache.end(), val))
		return true;

	long check = 0;
	long orig = val;
	long multiplier = 1;

	while (val != 0) {
		int digit = val % 10;
		check = check * 10 + digit;
		val /= 10;
	}

	if (orig == check) {
		AddToCache(orig);
		return true;
	}
	return false;
}