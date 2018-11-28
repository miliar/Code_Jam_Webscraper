#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        char s[200];
        scanf("%s ", s);
        int L = 0;
        while (s[L] == '-' || s[L] == '+') {
            L++;
        }
        char last = '0';
        int pos = 0;
        int zm = 0;
        while (pos < L) {
            last = s[pos];
            while (s[pos] == last) pos++;
            zm++;
        }
        if (last == '+') zm--;
        printf("Case #%d: %d\n", t+1, zm);

    }
    return 0;
}
