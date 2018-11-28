//============================================================================
// Name        : consonants.cpp
// Author      : amitabul
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

void printStr(char* str, int start, int end) {
	for (int i = start; i < end; i++) {
		printf("%c", str[i]);
	}
	printf("\n");
}
bool isOk(char* str, int start, int end, int minLength) {
	int foundCount = 0;
	bool started = false;
	//a, e, i, o, u
	for (int i = start; i < end; i++) {
		if (str[i] != 'a' && str[i] != 'e' && str[i] != 'i' && str[i] != 'o' && str[i] != 'u' ) {
			if (started == false) {
				started = true;
				foundCount = 1;
			} else {
				++foundCount;
			}
			if (foundCount >= minLength) {
				return true;
			}
		} else {
			started = false;
		}
	}
	return false;
}

int solve() {
	char inputStr[256];
	int minLength;
	scanf("%s %d", inputStr, &minLength);

	int strLength = strlen(inputStr);

	int resultCount = 0;

	for (int startPos = 0; startPos <= strLength - minLength; startPos++) {
		for (int endPos = startPos + minLength; endPos <= strLength; endPos++) {
			//printStr(inputStr, startPos, endPos);
			if (isOk(inputStr, startPos, endPos, minLength)) {
				++resultCount;
			}
		}
	}

	return resultCount;
}


int main()
{
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: %d\n", t, solve());
    }
    return 0;
}
