#include <bits/stdc++.h>

using namespace std;

int order[10] = {0, 2, 6, 4, 5, 7, 3, 1, 8, 9};
int let[10] = {'Z', 'W', 'X', 'U', 'F', 'V', 'R', 'O', 'T', 'I'};

int cnt[10];

string words[10] = {"ZERO", "TWO", "SIX", "FOUR", "FIVE", "SEVEN", "THREE", "ONE", "EIGHT", "NINE"};
int leters[26];

char s[100000];

int main() {
    int T;
    scanf("%d\n", &T);
    for (int test = 1; test <= T; ++test) {
        for (int i = 0; i < 10; ++i) {
            cnt[i] = 0;
        }
        for (int i = 0; i < 26; ++i) {
            leters[i] = 0;
        }

        gets(s);
        int len = strlen(s);
        for (int i = 0; i < len; ++i) {
            leters[s[i] - 'A']++;
        }

        for (int i = 0; i < 10; ++i) {
            cnt[order[i]] = leters[let[i] - 'A'];
            for (int j = 0; j < (int)words[i].size(); ++j) {
                leters[words[i][j] - 'A'] -= cnt[order[i]];
            }
        }

        /*cerr << test << endl;
        for (int i = 0; i < 26; ++i) {
            assert(leters[i] == 0);
        }*/

        printf("Case #%d: ", test);
        for (int i =0; i < 10;++i) {
            for (int j = 0; j < cnt[i]; ++j) {
                printf("%d", i);
            }
        }
        puts("");
    } 
}