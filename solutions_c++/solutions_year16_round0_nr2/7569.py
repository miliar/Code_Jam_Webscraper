#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<cmath>
#include<queue>
#include<stack>

using namespace std;

int main() {
    int t;
    scanf("%d",&t);
    char pattern[200];
    int caseNumber = 1;
    while (t--) {
        scanf("%s",pattern);
        int length = strlen(pattern);
        int startIndex = 0, endIndex = length - 1;
        //after each iteration check for end index
        for (int i = length - 1; i >= 0; i--) {
            if (pattern[i] != '+') {
                endIndex = i;
                break;
            }
        }

        int answer = 0;
        int countLength = 0;
        for (int i = 1; i < length; i++) {
            if (pattern[i] == '+') {
                countLength++;
            }
        }
        while ((endIndex != 0) && (countLength != length - 1)) {
            answer++;
            int secondPointer = 0;
            if (pattern[0] == '+') {
                for (int i = 0; i <= endIndex; i++) {
                    if (pattern[i] == '+') {
                        secondPointer = i;
                    }
                }
                //printf("Second pointer = %d  %s\n",secondPointer,pattern);

                char tempChar;
                for (int i = 0; i <= secondPointer; i++) {
                    if (pattern[i] == '+') {
                        pattern[i] = '-';
                    } else {
                        pattern[i] = '+';
                    }
                }
                if (secondPointer != 0) {
                    for (int i = 0; i < (secondPointer + 1)/2; i++) {
                        swap(pattern[i], pattern[secondPointer - i]);
                    }
                }
            } else {
                secondPointer = 0;
                for (int i = 0; i <= endIndex; i++) {
                    if (pattern[i] == '-') {
                        secondPointer = i;
                    }
                }

                char tempChar;
                for (int i = 0; i <= secondPointer; i++) {
                    if (pattern[i] == '+') {
                        pattern[i] = '-';
                    } else {
                        pattern[i] = '+';
                    }
                }
                if (secondPointer != 0) {
                    for (int i = 0; i < (secondPointer + 1)/2; i++) {
                        swap(pattern[i], pattern[secondPointer - i]);
                    }
                }
            }

            for (int i = length - 1; i >= 0; i--) {
                if (pattern[i] != '+') {
                    endIndex = i;
                    break;
                }
            }
            countLength = 0;
            for (int i = 1; i < length; i++) {
                if (pattern[i] == '+') {
                    countLength++;
                }
            }
            if (countLength == length - 1) {
                break;
            }
        }
        if (pattern[0] == '-') {
            answer++;
        }
        printf("Case #%d: %d\n",caseNumber,answer);
        caseNumber++;
    }
    return 0;
}