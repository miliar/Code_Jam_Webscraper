#include <algorithm>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

typedef vector<int> vi;

int calc(const vector<string>& v) {
    const int n = v.size();
    vi iv;
    For(i, n) iv.push_back(i);

    int freq[256] = {};
    For(i, v.size()) {
        For(j, v[i].length()) {
            freq[v[i][j]]++;
        }
    }

    int ans = 0;
    do {
        int used[256] = {};

        char prev = v[iv[0]][0];
        int cnt = 0;
        bool valid = true;
        For(i, n) {
            const string& s = v[iv[i]];
            For(j, s.length()) {
                char c = s[j];
                if (prev == c) {
                    cnt++;
                }
                else {
                    if (freq[prev] != cnt) {
                        valid = false;
                        goto END;
                    }

                    prev = c;
                    cnt = 1;
                }
            }
        }

        if (freq[prev] != cnt) {
            valid = false;
        }
        
    END:
        if (valid) ans++;

    } while (next_permutation(iv.begin(), iv.end()));

    return ans;
}

int main() {
    int ncases;
    scanf("%d", &ncases);
    For(cc, ncases) {
        int n;
        scanf("%d", &n);

        vector<string> v;
        For(i, n) {
            char s[1000];
            scanf("%s", s);
            v.push_back(s);
        }
        printf("Case #%d: %d\n", cc+1, calc(v));
    }
}

