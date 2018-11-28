#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <utility>
#include <set>
#include <map>
#include <cctype>

#define FOR(i,n) for(long long int i=0; i<n; i++)
#define MP(a,b) make_pair(a,b)
#define PB(x) push_back(x)
#define SORT(a) sort(a.begin(), a.end())
#define REV(a) reverse(a.begin(), a.end())

#define COND(p,t,f) ((p)?(t):(f))

#define PI 3.14159265

using namespace std;
typedef long long int lint;
typedef unsigned long long int ulint;



int main() {
    int T;
    cin >> T;
    FOR(t,T) {
        lint R,C;
        cin >> R >> C;
        vector <string> a;
        vector <lint> colCounts(C,0);
        vector <lint> rowCounts(R,0);
        FOR(i,R) {
            string s;
            cin >> s;
            a.PB(s);
        }

        FOR(i,R) {
            FOR (j,C) {
                if (a[i][j] != '.') {
                    colCounts[j]++;
                    rowCounts[i]++;
                }
                //cerr << a[i][j];
            }
            //cerr << endl;
        }

        cout << "Case #" << t+1 << ": ";

        bool imp = false;
        FOR (i,R) {
            FOR (j,C) {
                if (a[i][j] != '.' && colCounts[j]==1 && rowCounts[i]==1) {
                    imp = true;
                }
            }
        }

        if (imp) {
            cout << "IMPOSSIBLE" << endl;
            continue;
        }

        lint res = 0;

        FOR(i,R) {
            FOR (j,C) {
                if (a[i][j]!='.') {
                    int dr,dc;
                    if (a[i][j]=='>') {
                        dr = 0; dc = 1;
                    }
                    if (a[i][j]=='<') {
                        dr = 0; dc = -1;
                    }
                    if (a[i][j]=='^') {
                        dr = -1; dc = 0;
                    }
                    if (a[i][j]=='v') {
                        dr = 1; dc = 0;
                    }
                    int cr=i,cc=j;
                    lint pp=0;
                    while (cr>=0 && cr<R && cc>=0 && cc < C) {
                        if (a[cr][cc]!='.') pp++;
                        cr += dr;
                        cc += dc;
                    }
                    if (pp==1) res++;
                }
            }
        }


        cout << res << endl;

    }

}
