#include <fstream>
#include <iostream>
#include <vector>
#include <bitset>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <deque>

using namespace std;

const char infile[] = "input.in";
const char outfile[] = "output.out";

ifstream fin(infile);
ofstream fout(outfile);

const int MAXN = 55;
const int oo = 0x3f3f3f3f;

typedef vector<int> Graph[MAXN];
typedef vector<int> :: iterator It;

const inline int min(const int &a, const int &b) { if( a > b ) return b;   return a; }
const inline int max(const int &a, const int &b) { if( a < b ) return b;   return a; }
const inline void Get_min(int &a, const int b)    { if( a > b ) a = b; }
const inline void Get_max(int &a, const int b)    { if( a < b ) a = b; }

int N;
double C[MAXN], D[MAXN];

int main() {
    cin.sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);
    #endif
    int T;
    cin >> T;
    for(int test = 1 ; test <= T ; ++ test) {
        cout << "Case #" << test << ": ";

        int X = 0, Y = 0 ;
        cin >> N;
        cin >> fixed >> setprecision(5);
        for(int i = 1 ; i <= N ; ++ i)
            cin >> C[i];
        for(int i = 1 ; i <= N ; ++ i)
            cin >> D[i];
        sort(C + 1, C + N + 1);
        sort(D + 1, D + N + 1);
        int i = 1, j = 1;
        for( ; i <= N ; ++ i)
            if(C[i] > D[j]) {
                ++ X;
                ++ j;
            }
        i = 1; j = 1;
        for( ; i <= N ; ++ i)
            if(D[i] > C[j]) {
                ++ Y;
                ++ j;
            }
        Y = N - Y;
        cout << X << ' ' << Y << '\n';
    }
    fin.close();
    fout.close();
    return 0;
}
