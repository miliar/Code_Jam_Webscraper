#include <iostream>
#include <stdlib.h>
#include <stdio.h>

#define ll long long

using namespace std;

int m=0, n, ans;
string s;
char nor (char ch) {
    if (ch=='+') return '-';
    else return '+';
}

void findLen() {
    while (n>0 && s[n-1]=='+') n--;
}

void swapStrings( int k) {
    char ch;
    if (k==1) {
        s[0] = nor (s[0]);
        return;
    }
    else {
        for (int i=0;i<=(k-1)/2;i++) {
            ch = s[k-1-i];
            s[k-1-i] = nor(s[i]);
            s[i] = nor(ch);
        }
    }
}

int findLen1(int *start) {
    int i=0;
    while (i<n && s[i]=='+') i++;
    *start = i;
    while (i<n && s[i]=='-') i++;
    return i;
}

int findLen2(int *start) {
    int i =  n, maxo = 0, star, stari, c;
    while (i>0) {
        while (i>0 && s[i-1]=='-') i--;
        c = 0;
        stari = i;
        while (i>0 && s[i-1]=='+') {
            i--;
            c++;
        }
        if (c>maxo) {
            maxo = c;
            star = stari;
        }
    }
    *start = star;
    return maxo;
}

void compute() {
    if (s[m] == '-') {
        swapStrings(n);
    }
    else {
        int en1, en2;
        int a1 = findLen1(&en1);
        int a2 = findLen2(&en2);
        if (a1>a2) swapStrings(en1);
        else swapStrings(en2);
    }
}

int main() {
    int t, i;
    cin >> t;
    for (i=1;i<=t;i++) {
        cin >> s;
        n = s.length();
        findLen();
        ans = 0;
        while (n != 0) {
            ans++;
            compute();
            findLen();
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
