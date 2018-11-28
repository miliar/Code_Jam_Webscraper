#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define mt make_tuple
#define ll long long
#define pii pair<int,int>
#define tii tuple <int,int,int>
#define N 200005
#define mod 1000000005
#define X first
#define Y second
#define eps 0.0000000001
#define all(x) x.begin(),x.end()
#define tot(x) x+1,x+n+1
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int T, t, i, sol, n;
string s;

int main() {
    fin >> T;

    for(t = 1; t <= T; t++) {
        fin >> s;
        fout << "Case #" << t << ": ";
        n = s.size();
        sol = 0;

        if(n == 1) {
            if(s[0] == '-')
                fout << 1 << '\n';
            else
                fout << 0 << '\n';

            continue;
        }

        while(1) {
            for(i = 1; i < n; i++)
                if(s[i] != s[i - 1])
                    break;

            if(i == n) {
                if(s[n - 1] == '-')
                    sol++;

                break;
            }
            sol++;

            for(i--; i + 1; i--)
            {
                if(s[i] == '+')
                    s[i] = '-';
                else
                    s[i] = '+';
            }
        }

        fout << sol <<  '\n';
    }

    return 0;
}
