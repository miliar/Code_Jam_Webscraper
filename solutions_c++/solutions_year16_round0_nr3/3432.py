#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define ll long long int
#define s(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define sd(x) scanf("%lf", &x)
#define mod 1000000007
#define get getchar_unlocked

int isP[10000005];

void sieve()
{
    int i, j;
    isP[0] = isP[1] = 1;
    for (i = 2; i <= 10000000; ++i) {
        if (!isP[i]) {
            for (j = 2; i*j <= 10000000; ++j)
                isP[i*j] = 1;
        }
    }
}

int cnt;

void rec(int i, string &s)
{
    if (i == 16) {
        if (s[0] == '0' || s[15] == '0')
            return;
        int k = 0;
        for (i = 0; i < 16; ++i) {
            if (s[i] == '1')
                k += (1<<i);
        }
        if (!isP[k]) {
            ++cnt;
            cout << s << endl;
        }
        return;
    }
    s[i] = '0';
    rec(i+1, s);
    s[i] = '1';
    rec(i+1, s);
}

int main()
{
    sieve();
    string s;
    s.resize(16);
    rec(0, s);
    cout << cnt << endl;
}
