#include <cstdlib>
#include <cstdio>
#include <cstdint>
#include <cassert>

#define dbg(...) fprintf(stderr, __VA_ARGS__)

void flip(bool *buff, int l) {
    bool tmp[100];
    for (int i=0; i<l; i++) {
        tmp[i] = buff[i];
    }
    for (int i=0; i<l; i++) {
        buff[i] = not tmp[l-1-i];
    }
}

void fliptop(bool *buff) {
    assert(*buff == true);
    while(*buff == true) {
        *buff = false;
        buff++;
    }
}

void solve(bool *buff, int len) {
    unsigned n = 0;

    // Check if bottom is all happy-side-up. No manouvre needed.
    while (len > 0 && buff[len-1] == true)
        len--;

    while (len > 0) {
        assert(buff[len-1] == false);

        // If top starts with +, flip all consecutive pl
        if (buff[0] == true) {
            fliptop(buff);
            n++;
        }
        else {
            flip(buff, len);
            n++;
        }

        // Check if bottom is all happy-side-up. No manouvre needed.
        while (len > 0 && buff[len-1] == true)
            len--;
    }
    printf("%u\n", n);
}

int main() {
    int T;
    int len;
    bool buff[100];
    char s[101];
    scanf("%d", &T);
    for (int t=0; t<T; t++) {
        dbg("=== TEST %d ===\n", t+1);
        scanf("%s\n", s);
        for (len = 0; s[len] != 0; len++) {
            if (s[len] == '+')
                buff[len] = true;
            else if (s[len] == '-')
                buff[len] = false;
            else
                assert(false);
        }
        printf("Case #%d: ", t+1);
        solve(buff, len);
    }
}
