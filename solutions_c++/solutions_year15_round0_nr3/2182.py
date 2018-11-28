#include <cstdio>
#include <cstring>

using namespace std;

int T;
int L;
int X;
char ijks[10001];
char word[4] = "ijk";
int cache[10001][3][300];

char cal(char l, char r) {
    if(l < 0) return -cal(-l, r);
    if(r < 0) return -cal(l, -r);
    if(l == '1') return r;
    if(r == '1') return l;
    if(l == r) return -'1';
    if(l == 'i' && r == 'j') return 'k';
    if(l == 'i' && r == 'k') return -'j';
    if(l == 'j' && r == 'i') return -'k';
    if(l == 'j' && r == 'k') return 'i';
    if(l == 'k' && r == 'i') return 'j';
    if(l == 'k' && r == 'j') return -'i';
    return '?';
}

bool solve(int idx, int repeat, int wordIdx, char now) {
    if(wordIdx == 3) return false;
    if(idx == L && repeat == X) return wordIdx == 2 && now == 'k';
    if(idx == L && repeat < X) return solve(0, repeat + 1, wordIdx, now);

    int& ret = cache[(repeat - 1) * L + idx][wordIdx][now + 128];
    if(ret != -1) return ret;

    ret = 0;

    if(now == word[wordIdx]) {
        ret |= solve(idx, repeat, wordIdx + 1, '1');
    }

    ret |= solve(idx + 1, repeat, wordIdx, cal(now, ijks[idx]));

    return ret;
}

int main() {
    scanf("%d", &T);
    for(int c = 1; c <= T; c++) {
        scanf("%d %d", &L, &X);
        scanf("%s", ijks);
        memset(cache, -1, sizeof(cache));
        printf("Case #%d: %s\n", c, solve(0, 1, 0, '1') ? "YES" : "NO");
    }
    return 0;
}

