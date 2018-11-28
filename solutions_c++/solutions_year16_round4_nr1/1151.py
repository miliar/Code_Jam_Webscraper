#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <set>

using namespace std;

#define FOR(i, A, B) for(long long i=(A); i<(B); i++)
#define REP(i, N) for(long long i=0; i<(N); i++)
#define SZ(v) ((int)(v).size())
#define ALL(v) (v).begin(), (v).end()
#define SORT(v) sort(ALL(v))
#define CLEAR(v) memset((v), 0, sizeof(v))
#define MP make_pair
#define PB push_back
#define PII pair<int, int>
#define LL long long

string bestcomb(string a1, string a2, string b1, string b2) {
    string a = (a1<a2) ? a1+a2 : a2+a1;
    string b = (b1<b2) ? b1+b2 : b2+b1;
    return (a < b) ? a+b : b+a;
}

int main()
{
    int T;
    cin >> T;
    REP(caso, T) {
        cout << "Case #" << caso+1 << ": ";
        // cout << endl;

        int N, A, B, C;
        cin >> N >> B >> A >> C;
        int L = (1<<N);

        string a="A", b="B", c="C";
        int na = A, nb = B, nc = C;

        bool ok = true;
        string res = "";
        while(1) {

            // cout << a << " " << b << " " << c << endl;
            // cout << na << " " << nb << " " << nc << endl;

            if(L == 2) {
                if(na == 2 || nb == 2 || nc == 2) {
                    ok = false;
                    break;
                }

                if(na && nb) res = (a<b)?a+b:b+a;
                if(na && nc) res = (a<c)?a+c:c+a;
                if(nb && nc) res = (b<c)?b+c:c+b;

                break;
            }

            if(L == 1) {
                if(na) res = a;
                if(nb) res = b;
                if(nc) res = c;

                break;
            }


            int n = L/4;
            if(na < n || nb < n || nc < n) {
                ok = false;
                break;
            }

            string newa = bestcomb(a, b, a, c);
            string newb = bestcomb(a, b, b, c);
            string newc = bestcomb(a, c, b, c);

            int newna = na - n;
            int newnb = nb - n;
            int newnc = nc - n;

            a = newa;
            b = newb;
            c = newc;

            na = newna;
            nb = newnb;
            nc = newnc;

            L /= 4;
        }

        REP(i, SZ(res)) {
            if(res[i] == 'A') res[i] = 'P';
            if(res[i] == 'B') res[i] = 'R';
            if(res[i] == 'C') res[i] = 'S';
        }

        if(ok) cout << res << endl;
        else cout << "IMPOSSIBLE\n";



    }
}
