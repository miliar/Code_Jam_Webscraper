#include <cassert>
#include <climits>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

int calc(int n, char* s) {
    assert(n+1 == strlen(s));

    vector<int> v;
    int total = 0;
    for (int i = 0; i < n+1; i++) {
        v.push_back(s[i] - '0');
        total += v.back();
    }

    int invite = 0;
    int stand = v[0];
    for (int i = 1; i < v.size(); i++) {
        if (stand >= i) {
            stand += v[i];
        }
        else {
            invite += i-stand;
            stand += v[i] + (i-stand);
        }
    }
    return invite;
}

int main() {
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        int n;
        char s[2000];

        scanf("%d %s", &n, s);
        printf("Case #%d: %d\n", cc+1, calc(n, s));
    }
}

