#include <cstdio>
#include <cstring>
#include <algorithm>
#define infile "a.in"
#define outfile "a.out"
#define nMax 131
#define lMax 131
#define inf (1<<23)

using namespace std;

char v[nMax][lMax];
int n, ret;

void read() {
    scanf("%d\n", &n);

    for (int i = 0; i < n; ++i) {
        scanf("%s\n", v[i]);
    }
}

int reduce(char v[]) {
    int cnt = 0;

    for (int i = 1; i < strlen(v); ++i) {
        if (v[i] == v[i-1]) {
            cnt++;
        }

        v[i-cnt] = v[i];
    }

    v[strlen(v) - cnt] = 0;

    return cnt;
}

bool different(char a[], char b[]) {
    return strcmp(a, b) != 0;
}

int solve(char a[], char b[]) {

    int cnt = 0;
    int ita = 0, itb = 0;

    if (a[0] != b[0]) {
        return -1;
    }

    while (ita < strlen(a) && itb < strlen(b)) {
        if (a[ita] != b[itb]) {

            ++cnt;

            if (a[ita-1] == a[ita]) {
                ++ita;
            } else if (b[itb-1] == b[itb]) {
                ++itb;
            } else {
                return -1;
            }
        } else {
            ita++, itb++;
        }
    }

    while (ita < strlen(a)) {
        if (a[ita] != a[ita-1]) {
            return -1;
        }

        ++ita, ++cnt;
    }

    while (itb < strlen(b)) {
        if (b[itb] != b[itb-1]) {
            return -1;
        }

        itb++, ++cnt;
    }

    return cnt;
}

int solve(int crt) {
    int cnt = 0;

    for (int i = 0; i < n; ++i) {
        int x = solve(v[i], v[crt]);

        if (x == -1) {
            return inf;
        }

        cnt += x;
    }

    return cnt;
}

void solve() {
    ret = inf;

    for (int i = 0; i < n; ++i) {
        ret = min(ret, solve(i));
    }
}

void write(int t) {
    printf("Case #%d: ", t);

    if (ret != inf) {
        printf("%d\n", ret);
    } else {
        printf("Fegla Won\n");
    }
}

int main() {
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);

    int t;
    scanf("%d\n", &t);

    for (int i = 0; i < t; ++i) {
        read();
        solve();
        write(i+1);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
