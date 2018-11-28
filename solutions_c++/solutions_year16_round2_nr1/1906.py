#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define RREP(i,s,e) for (i = s; i >= e; i--)
#define rrep(i,n) RREP(i,n-1,0)
#define REP(i,s,e) for (i = s; i <= e; i++)
#define rep(i,n) REP(i,0,n-1)
#define INF 100000000

typedef long long ll;

int num[10], chr[26];
string ns[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void dec(char c, int n) {
    int i;
    int x = chr[c-'A'];
    num[n] += x;
    rep (i,ns[n].size())
        chr[ns[n][i]-'A'] -= x;
}

int main() {
    int i, t;
    cin >> t;
    rep (i,t) {
        string s;
        int j, k;
        cin >> s;
        fill(num,num+10,0);
        fill(chr,chr+26,0);
        cout << "Case #" << i+1 << ": ";
        for (auto c : s)
            chr[c-'A']++;
        dec('Z',0);
        dec('G',8);
        dec('X',6);
        dec('U',4);
        dec('W',2);
        dec('R',3);
        dec('O',1);
        dec('S',7);
        dec('V',5);
        dec('I',9);
        rep (j,10) rep (k,num[j]) cout << j;
        cout << endl;
    }
    return 0;
}
