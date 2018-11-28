#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
const int N = 10005;

struct Node {
    int s;
    char c;
    Node () {}
    Node (int s, char c):s(s), c(c) {}

    Node operator * (const Node & a) const {
        Node ret = Node (s * a.s, 0);
        if (c == '1') {
            ret.c = a.c;
        }
        else {
            if (a.c == '1') {
                ret.c = c;
            }
            else {
                if (a.c == c) {
                    ret.c = '1';
                    ret.s *= -1;
                }
                else {
                    if (c == 'i' && a.c == 'j') {
                        ret.c = 'k';
                    }
                    if (c == 'i' && a.c == 'k') {
                        ret.c = 'j';
                        ret.s *= -1;
                    }
                    if (c == 'j' && a.c == 'i') {
                        ret.c = 'k';
                        ret.s *= -1;
                    }
                    if (c == 'j' && a.c == 'k') {
                        ret.c = 'i';
                    }
                    if (c == 'k' && a.c == 'i') {
                        ret.c = 'j';
                    }
                    if (c == 'k' && a.c == 'j') {
                        ret.c = 'i';
                        ret.s *= -1;
                    }
                }
            }
        }
        return ret;
    }
    bool operator == (const Node &a) const{
        return c == a.c && s == a.s;
    }
};

char str[N];

int main () {
//    freopen("C-small-attempt0.in", "r" ,stdin);
//    freopen("out.txt", "w", stdout);
    int cases;
    cin >> cases;
    int L, X;
    for (int cas = 1; cas <= cases; cas ++) {
        scanf ("%d %d", &L, &X);
        scanf ("%s", str);
        Node a(1, '1');
        Node b(1, '1');
        Node c(1, '1');
        printf ("Case #%d: ", cas);
        LL la = 0, ra = 0;
        bool flag = 0, fa = 0, fb = 0, fc = 0;
        Node tmp(1, '1');
        for (ra = 0; ra < X * L && (ra - la) / L < 4; ra ++) {
            int pos = ra % L;
            tmp = tmp * Node(1, str[pos]);
            if (tmp == Node(1, 'i')) {
                fa = 1;
                ra++;
                break;
            }
        }
        if (!fa) {
            puts("NO");
            continue;
        }
        LL lb = ra, rb = ra;
        tmp = Node(1, '1');
        for (rb = ra; rb < X * L && (rb - lb) / L < 4; rb++) {
            int pos = rb % L;
            tmp = tmp * Node(1, str[pos]);
            if (tmp == Node(1, 'j')) {
                fb = 1;
                rb++;
                break;
            }
            //cout << rb << " " << tmp.c <<endl;
        }
        if (!fb) {
            puts("NO");
            continue;
        }
        LL lc = rb, rc = rb;
        tmp = Node(1, '1');
        int num = (X - (rb / L)) % 4;
        for (rc = rb % L; rc < num * L; rc ++) {
            int pos = rc % L;
            tmp = tmp * Node(1, str[pos]);

        }
        if (tmp == Node(1, 'k')) {
            fc = 1;
            puts("YES");
        }
        else {
            puts("NO");
        }

    }

    return  0;
}
