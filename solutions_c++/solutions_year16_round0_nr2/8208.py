#include <stdio.h>
#include <string.h>
#define REP(a, b) for (int a = 0; a < b; a++)
#define FORU(a, b, c) for (int a = b; a <= c; a++)
using namespace std;

int main() {
int T, n;
char S[105];

scanf("%d", &T);

FORU(tc, 1, T) {
scanf("%s", S);

int len = strlen(S);
int numOfStack = 1;

FORU(i, 1, len - 1) {
if (S[i] != S[i-1]) {
numOfStack++;
}
}

if (S[len-1] == '+') {
numOfStack--;
}

printf("Case #%d: %d\n", tc, numOfStack);
}

return 0;
}