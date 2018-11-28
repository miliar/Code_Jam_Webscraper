#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include<conio.h>

#define ll long long

using namespace std;

int m=0, n, ans;
string s;
char nor (char ch) {
    if (ch=='+') return '-';
    else return '+';
}

void getLengthFromLast() {
    while (n>0 && s[n-1]=='+') n--;
}

void swapS( int k) {
    char ch;
    if (k==1) {
        s[0] = nor (s[0]);
        //cout << s[0];
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

void operate() {
    if (s[m] == '-') {
        //cout << "Case 1" << endl;
        swapS(n);
    }
    else {
        int en1, en2;
        int a1 = findLen1(&en1);
        int a2 = findLen2(&en2);
        if (a1>a2) swapS(en1);
        else swapS(en2);
        //cout << "Case 2" << a1 << " : " <<a2 << endl;
    }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output2-large.out", "w", stdout);
    int t, i;
    cin >> t;
    for (i=1;i<=t;i++) {
        cin >> s;
        n = s.length();
        getLengthFromLast();
        //cout << s << " : " << n << endl;
        ans = 0;
        while (n != 0) {
            ans++;
            operate();
            //cout << "Inside : " << s << " : " << n << endl; getch();
            getLengthFromLast();
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
