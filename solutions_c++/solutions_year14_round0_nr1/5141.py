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

const int MAXN = 100005;
const int oo = 0x3f3f3f3f;

typedef vector<int> Graph[MAXN];
typedef vector<int> :: iterator It;

const inline int min(const int &a, const int &b) { if( a > b ) return b;   return a; }
const inline int max(const int &a, const int &b) { if( a < b ) return b;   return a; }
const inline void Get_min(int &a, const int b)    { if( a > b ) a = b; }
const inline void Get_max(int &a, const int b)    { if( a < b ) a = b; }

bitset <20> Used;

int main() {
    cin.sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);
    #endif
    int T;
    cin >> T;
    for(int test = 1 ; test <= T ; ++ test) {
        Used.reset();
        int x;
        cin >> x;
        for(int i = 1 ; i <= 4 ; ++ i) {
            int y;
            for(int j = 1 ; j <= 4 ; ++ j) {
                cin >> y;
                if(i == x)
                    Used[y] = 1;
            }
        }
        int ans = 0;
        cin >> x;
        for(int i = 1 ; i <= 4 ; ++ i) {
            int y;
            for(int j = 1 ; j <= 4 ; ++ j) {
                cin >> y;
                if(i == x && Used[y]) {
                    if(!ans)
                        ans = y;
                        else ans = -1;
                }
            }
        }
        cout << "Case #" << test << ": ";
        if(ans == -1)
            cout << "Bad magician!\n";
        if(ans == 0)
            cout << "Volunteer cheated!\n";
        if(ans != 0 && ans != -1)
            cout << ans << "\n";
    }
    fin.close();
    fout.close();
    return 0;
}
