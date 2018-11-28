#include <bits/stdc++.h>

#define uint unsigned int
#define INF 999999999
#define LINF 999999999999999999
#define ll long long
#define ld long double
#define M 1000000007
#define E 0.0000001
#define N (1<<17)
#define pii pair<int, int>
#define pll pair<long long, long long>
#define pdd pair<double, double>
#define ull unsigned long long
#define C 'a'

using namespace std;

int main() {
    ifstream in("google.in");
    ofstream out("google.out");

    int t;
    in>>t;
    for (int c = 1; c <= t; c++) {
        string s;
        in>>s;
        int ans = 1;
        for (int i = 1; i < s.length(); i++) {
            if (s[i] != s[i - 1]) ans++;
        }
        if (s[s.length() - 1] == '+') ans--;
        out<<"Case #"<<c<<": "<<ans<<endl;
    }
    out.close();
}
