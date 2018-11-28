#include <map>
#include <set>
#include <queue>
#include <time.h>
#include <string>
#include <math.h>
#include <vector>
#include <cstring>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <algorithm>
const int inf = 1000000000,
          mod = 1000000007;
#define Wi(a) printf("%d ", (a))
#define Wi2(a, b) printf("%d %d ", (a), (b))
#define Wie(a) printf("%d\n", (a))
#define Wie2(a, b) printf("%d %d\n", (a), (b))
#define Ri(a) scanf("%d", &(a))
#define Ri2(a, b) scanf("%d%d", &(a), &(b))
#define F first
#define S second
#define pii pair < int, int >
#define v(tp) vector< tp >
#define ll long long
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for(int (i) = (a), _n_ = (b); (i) <= _n_; (i)++)
#define FORD(i,a,b) for(int (i) = (a), _n_ = (b); (i) >= _n_; (i)--)
#define forn(i,b) FOR((i),0,(b) - 1)
using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    Ri(t);
    int mas[4][4], used[20];
    forn(q, t) {
        memset( used, 0, 80 );
        int p;
        forn(s,2) {
            Ri(p);
            p--;
            forn( i, 4 ) {
                forn( j, 4 ) {
                    Ri(mas[i][j]);
                }
            }
            forn( j, 4 ) {
                used[mas[p][j]]++;
            }
        }
        printf("Case #%d: ", q + 1);
        if( count( used, used + 20, 2 ) == 1 ) {
            Wie( (int)(find(used, used + 20, 2) - used) );
        } else {
            if( count( used, used + 20, 2 ) > 1 ) {
                puts("Bad magician!");
            } else {
                puts("Volunteer cheated!");
            }
        }
    }
    return 0;
}
