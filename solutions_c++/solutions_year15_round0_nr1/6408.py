#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace::std;

int main(int argc, char** argv) {
    int t, tc = 1;
    cin >> t;
    while (t--) {
        int s;
        cin >> s;
        int p[s + 1];
        for (int i = 0; i <= s; i++) {
            scanf("%1d", &p[i]);
        }

        int standing = p[0], required = 0;

        for (int i = 1; i <= s; i++) {
            if (p[i] != 0 && i > standing) {
                required += i - standing;
                standing += i - standing;
            }
            standing += p[i];
        }

        printf("Case #%d: %d\n", tc++, required);
    }
    return 0;
}

