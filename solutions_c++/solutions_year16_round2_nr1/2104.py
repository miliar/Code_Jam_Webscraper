#include <iostream>
#include <cstdio>
#include <cstring>
#include <numeric>
#include <algorithm>

using namespace std;

typedef long long i64;

#define edge(i, u) for (int i = head[u]; i != -1; i = graph[i].next)
#define range(i, a, b, step) for (int i = ((int) (a)); i != ((int) (b)) && ((i - ((int) (b))) ^ ((int) (step))) < 0 ; i += ((int) (step)))

string a;
int tcase, times = 0, cnt[26], num[10];

int main(int argc, char const *argv[]) {
#ifndef ONLINE_JUDGE
    // freopen("ap.txt","r",stdin);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif

    cin >> tcase;
    while (tcase > times++) {
        cin >> a;
        memset(cnt, 0, sizeof cnt);
        for (int i = 0; a.length() > i; i++) {
            cnt[a[i] - 'A']++;
        }
        num[0] = cnt['Z' - 'A'];
        num[2] = cnt['W' - 'A'];
        num[4] = cnt['U' - 'A'];
        num[6] = cnt['X' - 'A'];
        num[8] = cnt['G' - 'A'];
        num[5] = cnt['F' - 'A'] - num[4];
        num[3] = cnt['H' - 'A'] - num[8];
        num[7] = cnt['S' - 'A'] - num[6];
        num[9] = cnt['I' - 'A'] - num[5] - num[6] - num[8];
        num[1] = cnt['N' - 'A'] - num[7] - 2 * num[9];
        cout << "Case #" << times << ": ";
        range(i, 0, 10, 1) range(j, 0, num[i], 1) {
            cout << i;
        }
        cout << endl;
    }

    return 0;
}