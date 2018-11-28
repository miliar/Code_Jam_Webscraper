#include <iostream>
#include <cstdio>
#include <list>
using namespace std;

int l;
int start;

void printb(bool b[10]) {
    for (int i = 0; i<l; i++) printf("%c", (b[i] ? '1' : '0'));
    printf("\n");
}

int getId(bool b0[10], int rot) {
    rot++;
    bool b[10]; for (int i = 0; i<l; i++) b[i] = b0[i];
    //printb(b);
    for (int i = 0; i<rot/2; i++) {
        swap(b[i], b[rot-i-1]);
    }

    //printb(b);
    for (int i = 0; i<rot; i++) b[i] = !b[i];
    //printb(b);

    int ans = 0;
    for (int i = 0; i<l; i++) {
        ans *= 2;
        if (b[i]) ans++;
    }

    return ans;
}

list<int> neighbours(int x) {
    if (x == 2047) printf("neighbours of %d: \n", x);
    list<int> ans;

    bool b[10];
    for (int i = l-1; i>=0; i--) {
        b[i] = x%2==1;
        x/=2;
    }

    for (int i = 0; i<l; i++) {
        int val = getId(b, i);
        if (x == 2047) printf("                     rotating %d: %d\n", i, val);
        ans.push_back(val);
    }
    return ans;
}

bool be[2050];


int calculate () {
    //printf("start %d, l %d\n", start, l);

    if (start == 0) return 0;

    int sk=0; int sv=0; int sor[2050];
    sor[0] = start;
    int d[2050]; d[start] = 0;

    while (sk<=sv) {
        int akt = sor[sk++];
        //printf("%d\n", akt);
        if (akt == 0) return d[akt];
        list<int> neigh = neighbours(akt);
        for (list<int>::iterator it = neigh.begin(); it != neigh.end(); it++) {
            int to = *it;

            if (be[to]) continue;

            be[to] = true;
            d[to] = d[akt]+1;
            sor[++sv] = to;
            //printf("neighbour %d -> %d\n", akt, to);
        }
    }
    return -1;
}

void read() {
    char c; scanf("%c", &c);
    l=0;
    bool st[10];
    while (c == '+' || c == '-') {
        st[l] = c == '-';
        l++;
        scanf("%c", &c);
    }
    int ans = 0;
    for (int i = 0; i<l; i++) {
        ans *= 2;
        if (st[i]) ans++;
    }
    start = ans;
    for (int i = 0; i<2050; i++) be[i] = false;
}

int main()
{
    //freopen("in.txt", "r", stdin);
    int n;
    scanf("%d\n", &n);
    for (int i=0; i<n; i++) {
        //scanf("%c");
        read();
        printf("Case #%d: %li\n", i+1, calculate());
    }

    return 0;
}
