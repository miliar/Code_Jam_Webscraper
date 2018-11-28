#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#define pb push_back
using namespace std;

char win(char c1, char c2) {
    if (c1 == c2) {
        return '\0';
    }

    if (c1 == 'P') {
        if (c2 == 'R') {
            return c1;
        } else {
            return c2;
        }
    } else if (c1 == 'R') {
        if (c2 == 'P') {
            return c2;
        } else {
            return c1;
        }
    } else {
        if (c2 == 'P') {
            return c1;
        } else {
            return c2;
        }
    }
}

int check(string a) {
    if ((int)a.size() == 1) {
        return 1;
    }

    string b = "";
    for (int i = 0; i < (int)a.size(); i += 2) {
        char c = win(a[i], a[i + 1]);
        if (c != '\0') {
            b += c;
        } else {
            return 0;
        }
    }
    return check(b);
}


int main(void) {
    int t;
    int n, r, p, s;

    scanf(" %d", &t);
    for (int caso = 1; caso <= t; caso++) {
        scanf(" %d %d %d %d", &n, &r, &p, &s);
        string a = "";
        string res = "";
        for (int i = 0; i < r; i++) {
            a += 'R';
        }
        for (int i = 0; i < p; i++) {
            a += 'P';
        }
        for (int i = 0; i < s; i++) {
            a += 'S';
        }

        sort(a.begin(), a.end());
        do {
            if (check(a)) {
                //cout << "here a = " << a << endl;
                if (res == "" || a < res) {
                    res = a;
                }
            }
        }while(next_permutation(a.begin(), a.end()));

        printf("Case #%d: ", caso);
        if (res == "") {
            printf("IMPOSSIBLE\n");
        } else {
            cout << res << endl;
        }
    }
    return 0;
}

