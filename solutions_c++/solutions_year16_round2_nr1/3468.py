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

int mrk[30];

vector <int> v[20];

void pre()
{
    int i;
    string s;
    s = "ZERO";
    for (i = 0; i < s.size(); ++i)
        v[0].pb(s[i]-65);
    s = "ONE";
    for (i = 0; i < s.size(); ++i)
        v[1].pb(s[i]-65);
    s = "TWO";
    for (i = 0; i < s.size(); ++i)
        v[2].pb(s[i]-65);
    s = "THREE";
    for (i = 0; i < s.size(); ++i)
        v[3].pb(s[i]-65);
    s = "FOUR";
    for (i = 0; i < s.size(); ++i)
        v[4].pb(s[i]-65);
    s = "FIVE";
    for (i = 0; i < s.size(); ++i)
        v[5].pb(s[i]-65);
    s = "SIX";
    for (i = 0; i < s.size(); ++i)
        v[6].pb(s[i]-65);
    s = "SEVEN";
    for (i = 0; i < s.size(); ++i)
        v[7].pb(s[i]-65);
    s = "EIGHT";
    for (i = 0; i < s.size(); ++i)
        v[8].pb(s[i]-65);
    s = "NINE";
    for (i = 0; i < s.size(); ++i)
        v[9].pb(s[i]-65);
}

bool check()
{
    int i;
    for (i = 0; i < 26; ++i) {
        if (mrk[i])
            return false;
    }
    return true;
}

string toString(int i)
{
    string x;
    x.pb(i+48);
    return x;
}

int tmp[26];

bool func(int i, string num)
{
    //cout << i << " " << num << endl;
    if (i == 10) {
        if (check()) {
            cout << num << endl;
            return true;
        }
        return false;
    }
    int j;
    bool found;
    for (j = 0; j < 26; ++j)
        tmp[j] = mrk[j];
    found = true;
    for (j = 0; j < v[i].size(); ++j) {
        if (tmp[v[i][j]]) {
            --tmp[v[i][j]];
        }
        else {
            found = false;
            break;
        }
    }
    if (found) {
        for (j = 0; j < v[i].size(); ++j)
            --mrk[v[i][j]];
        if (func(i, num+toString(i)))
            return true;
        for (j = 0; j < v[i].size(); ++j)
            ++mrk[v[i][j]];
    }
    return func(i+1, num);
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, u = 0, i;
    pre();
    string num, s;
    cin >> t;
    while (t--) {
        num = "";
        for (i = 0; i < 26; ++i)
            mrk[i] = 0;
        cin >> s;
        for (i = 0; i < s.size(); ++i)
            ++mrk[s[i]-65];
        printf("Case #%d: ", ++u);
        func(0, num);
    }
    return 0;
}
