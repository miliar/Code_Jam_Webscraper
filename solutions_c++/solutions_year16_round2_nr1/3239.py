#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using  namespace std;

const int N = 2100;

int cnt[30];
int cnt2[30];
int in[30];

void update(string names[], int index) {
    memset(cnt2, 0, sizeof(cnt2));
    memset(in, 0, sizeof(in));

    for(auto c: names[index]) {
        in[c - 'A'] = 1;
        cnt2[c - 'A'] += 1;
    }

    for(char c = 'A'; c <= 'Z'; c++) {
        if(!in[c - 'A']) continue;
        cnt[c - 'A'] -= cnt2[c - 'A'];
    }
}

int has(string names[], int index) {

    memset(cnt2, 0, sizeof(cnt2));
    memset(in, 0, sizeof(in));

    for(auto c: names[index]) {
        in[c - 'A'] = 1;
        cnt2[c - 'A'] += 1;
    }

    int ok = 1;

    for(char c = 'A'; c <= 'Z'; c++) {
        if(!in[c - 'A']) continue;
        ok &= ((cnt[c - 'A'] >= cnt2[c - 'A']) ? 1 : 0);
    }

    return ok;
}

int main( void ) {

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    string names[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    string digits[] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

    int t;
    int tt = 1;

    cin >> t;
    while(t--) {

        cout << "Case #" << tt++ << ": ";

        string s;
        cin >> s;

        memset(cnt, 0, sizeof(cnt));
        int n = (int)s.size();

        for(int i = 0; i < n; i++)
            cnt[ s[i] - 'A' ] += 1;

        string ans;

        while(cnt['X' - 'A']) {
           ans += '6';
           update(names, 6);
        }

        while(cnt['W' - 'A']) {
            ans += '2';
           update(names, 2);
        }

        while(cnt['Z' - 'A']) {
            ans += '0';
           update(names, 0);
        }

        while(cnt['U' - 'A']) {
            ans += '4';
           update(names, 4);
        }

        while(cnt['O' - 'A']) {
            ans += '1';
           update(names, 1);
        }

        while(cnt['G' - 'A']) {
            ans += '8';
           update(names, 8);
        }

        while(cnt['F' - 'A']) {
            ans += '5';
           update(names, 5);
        }

        while(cnt['H' - 'A']) {
            ans += '3';
           update(names, 3);
        }

        while(cnt['V' - 'A']) {
            ans += '7';
           update(names, 7);
        }

        while(cnt['E' - 'A']) {
            ans += '9';
           update(names, 9);
        }

        sort(ans.begin(), ans.end());
        cout << ans << endl;
    }

    return 0;
}
