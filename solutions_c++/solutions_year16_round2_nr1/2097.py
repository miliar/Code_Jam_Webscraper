#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <cstring>

using namespace std;

const int maxN = 1000010;

#define foru(i, l, r) for (int i = l; i <= r; ++i)
#define ford(i, r, l) for (int i = r; i >= l; --i)
#define repu(i, r) for (int i = 0; i < r; ++i)
#define F first
#define S second
#define ll long long

int a[] = {0, 2, 6, 7, 4, 5, 3, 8, 1, 9};
string s[] = {"ZERO", "TWO", "SIX", "SEVEN", "FOUR", "FIVE", "THREE", "EIGHT", "ONE", "NINE"};
char c[] = {'Z', 'W', 'X', 'S', 'U', 'F', 'R', 'T', 'O', 'E'};
int num[30], res[20], test;
char st[2010];

void get_num(int d, string s, char c) {
    int len = s.length();
    int temp = num[c - 'A'];
    res[d] += num[c - 'A'];
    repu(i, len)
        num[s[i] - 'A'] -= temp;
}

int main() {
    freopen("out.txt", "w", stdout);
    scanf("%d\n", &test);
    int t = 0;
    while (test--) {
        ++t;
        scanf("%s\n", st);
        int len = strlen(st);
        repu(i, 26) num[i] = 0;
        repu(i, 10) res[i] = 0;
        repu(i, len) ++num[st[i] - 'A'];
        repu(i, 10) get_num(a[i], s[i], c[i]);
        printf("Case #%d: ", t);
        repu(i, 10)
            repu(j, res[i]) printf("%d", i);
        cout << endl;
    }
    fclose(stdout);
}
