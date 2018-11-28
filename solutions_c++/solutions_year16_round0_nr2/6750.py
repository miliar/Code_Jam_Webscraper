#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int T;
int len;
int ans;
int pans[1010];
char pansString[1010];

void flip(int l, int r) {
    for (int i = l; i <= r; ++i)
        pans[i] = 1 - pans[i];
    for (; l < r;) {
        swap(pans[l], pans[r]);
        ++ l;
        -- r;
    }
}

void flipSadSide() {
    for (int i = len - 1; i >= 0; --i) {
            if (pans[i] == 0) {
                flip(0, i);
                break;
            }
    }
}

void flipHappySide() {
    for (int i = 0; i < len; ++i) {
        if (pans[i] == 0) {
            flip(0, i - 1);
            break;
        }
    }
}

int check() {
    for (int i = 0; i < len; ++i) {
        if (pans[i] == 0) {
            return false;
        }
    }
    return true;
}

int main()
{
    freopen("B_large.in", "r", stdin);
    freopen("B_large.out", "w", stdout);

    scanf("%d\n", &T);
    for (int Cas = 1; Cas <= T; ++Cas) {
        scanf("%s\n", pansString);

        len = strlen(pansString);

        for (int i = 0; i < len; ++i) {
            if (pansString[i] == '-') {
                pans[i] = 0;
            } else {
                pans[i] = 1;
            }
        }

        ans = 0;
        while (true) {
            if (check()) {
                break;
            }

            if (pans[0] == 0) {
                flipSadSide();
            } else {
                flipHappySide();
            }

            ++ans;
        }

        printf("Case #%d: %d\n", Cas, ans);
    }


    return 0;
}
