#include <stdio.h>
#include <string.h>
#define REP(a, b) for (int a = 0; a < b; a++)
#define FORU(a, b, c) for (int a = b; a <= c; a++)
using namespace std;

int main() {
int T, n;

scanf("%d", &T);

FORU(tc, 1, T) {
scanf("%d", &n);

bool done, flag[11];

memset(flag, 0, sizeof(flag));
int findDigit = 0;
int temp = 0;

while (findDigit != 10 && n != 0) {
temp += n;

int temp2 = temp;

while (temp2 != 0) {
int digit = temp2 % 10;
temp2 /= 10;

if (!flag[digit]) {
flag[digit] = true;
findDigit++;
}
}
}

if (n == 0) {
printf("Case #%d: INSOMNIA\n", tc);
}
else {
printf("Case #%d: %d\n", tc, temp);
}
}

return 0;
}