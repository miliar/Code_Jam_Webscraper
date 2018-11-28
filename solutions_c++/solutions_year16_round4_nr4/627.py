#include <bits/stdc++.h>

using namespace std;
using LINT = long long int;
using PII = pair<int,int>;

#define PB push_back
#define FI first
#define SE second
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i, a, b) for(int i=(a);i<(b);++i)

int n;
bitset<16> workers;

bool machrec[7];
bool works[7];

bool globgok;

bool reccheck(int c, bitset<16> & test) {
    if(c >= n) return true;

    // cout << c << ' ';

    bool gok = true;
    REP(w, n) {
        if(works[w]) continue;

        works[w] = 1;

        bool ok = false;
        REP(x, n) {
            if(test[w*n+x] && machrec[x] == 0) {
               machrec[x] = 1;
               if(reccheck(c + 1, test))
                    ok = true;
               machrec[x] = 0;
            }
        }

        if(!ok) {
            gok = false;
            break;
        }

        works[w] = 0;
    }

    if(!gok) globgok = false;


    // cout << 'x' << gok << endl;

    return gok;
}

void process(int caseNum) {
    cin >> n;
    int r = 0;



    // cout << n << endl;

    workers.reset();

    REP(i, n) {
        string s;
        cin >> s;
        REP(j, n)
            workers[r*n+j] = s[j] == '1';
        r++;
    }

    int lemin = 500;

    REP(x, (1<<(n*n))) {
        bitset<16> test(x);

        bool ok = true;
        REP(z, n*n)
            if(test[z] == 0 && workers[z] == 1) ok = false;

        if(!ok) continue;

        REP(z, n) {
            bool gok = false;
            REP(y, n)
                if(test[y*n+z]) gok = true;

            if(!gok) ok = false;
        }


        if(!ok) continue;

        // if(test.count() < workers.count())
            // cout << test << ' ' << workers << endl;

        int dollars = test.count() - workers.count();



        memset(machrec, 0, sizeof machrec);
        memset(works, 0, sizeof works);

        globgok = true;
        reccheck(0, test);

        if(globgok) {
            // if(dollars == 2) cout << test << endl;
            lemin = min(lemin, dollars);
        }
    }

    cout << "Case #" << caseNum << ": " << lemin << endl;
}


int main() {
   /*n = 3;
    bitset<16> foo("0000000100011100");
    cout << foo << endl;
    reccheck(0, foo);
    return 0;*/

    int t;
    cin >> t;
    REP(i, t) process(i+1);

    return 0;
}
