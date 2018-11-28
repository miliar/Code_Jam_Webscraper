#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <cstring>
using namespace std;

#define N 10005
#define MII map<int, int>
#define ITER_MII map<int, int>::iterator
#define PCI pair<char, int>
#define MP(a, b) make_pair(a, b)

char ch[N];
int n;
PCI product[N];

void read() {
    int L, X;
    scanf("%d%d", &L, &X);
    scanf("%s", ch);
    n = L * X;
    int pos = L;

    for (int i = 0; i < X - 1; i++) {
        for (int j = 0; j < L; j++)
            ch[pos++] = ch[j];
    }
    ch[pos] = '\0';
}

PCI multiply(const PCI& lh, const PCI& rh) {
    int flag = lh.second * rh.second;
    char c = '1';

    if (lh.first == '1' || rh.first == '1')
        c = (lh.first == '1') ? rh.first : lh.first;
    else if (lh.first == rh.first) {
        c = '1';
        flag *= -1;  // tricky
    } else if (lh.first == 'i') {
        if (rh.first == 'j')
            c = 'k';
        else {
            c = 'j';
            flag *= -1;
        }
    } else if (lh.first == 'j') {
        if (rh.first == 'i') {
            c = 'k';
            flag *= -1;
        } else
            c = 'i';
    } else {
        if (rh.first == 'i')
            c = 'j';
        else {
            c = 'i';
            flag *= -1;
        }
    }
    return MP(c, flag);
}

bool solve() {
    if (n < 3)
        return false;

    product[0] = MP(ch[0], 1);
    for (int i = 1; i < n; i++)
        product[i] = multiply(product[i - 1], MP(ch[i], 1));

    if (product[n - 1] != MP('1', -1))
        return false;

    PCI const_i = MP('i', 1);
    PCI const_k = MP('k', 1);
    for (int i = 0; i < n - 2; i++) {
        if (product[i] == const_i) {
            for (int j = i + 1; j < n - 1; j++) {
                if (product[j] == const_k)
                    return true;
            }
        }
    }
    return false;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int kase;
    scanf("%d", &kase);
    for (int kase_no = 1; kase_no <= kase; kase_no++) {
        read();
        printf("Case #%d: %s\n", kase_no, solve() ? "YES" : "NO");
    }
    return 0;
}
