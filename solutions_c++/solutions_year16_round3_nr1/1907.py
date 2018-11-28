#include <iostream>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int n, ans;
string str;

char change (char c) {
    if (c=='-') return '+';
    else return '-';
}

void rotate( int m) {
    char c;
    if (m==1) {
        str[0] = change (str[0]);
        return;
    }
    else {
        for (int i=0;i<=(m-1)/2;i++) {
            c = str[m-1-i];
            str[m-1-i] = change(str[i]);
            str[i] = change(c);
        }
    }
}

int findPos() {
    int a1=0, star1;
    while (a1<n && str[a1]=='+') a1++;
    star1 = a1;
    while (a1<n && str[a1]=='-') a1++;

    int i =  n, a2 = 0, star2, stari, counti;
    while (i>0) {
        while (i>0 && str[i-1]=='-') i--;
        counti = 0;
        stari = i;
        while (i>0 && str[i-1]=='+') {
            i--;
            counti++;
        }
        if (counti>a2) {
            a2 = counti;
            star2 = stari;
        }
    }

    if (a1>a2) return star1;
    else return star2;
}

int main() {
    freopen("B-large-.in", "r", stdin);
    freopen("output2-large-.out", "w", stdout);
    int t, i;
    cin >> t;
    for (i=1;i<=t;i++) {
        cin >> str;
        n = str.length();
        while (n>0 && str[n-1]=='+') n--;
        ans = 0;
        while (n != 0) {
            ans++;
            if (str[0] == '-') {
                rotate(n);
            }
            else {
                int en = findPos();
                rotate(en);
            }
            while (n>0 && str[n-1]=='+') n--;
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
