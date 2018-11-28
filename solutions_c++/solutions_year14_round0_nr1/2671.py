#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
#define sz(c) (int)(c).size()
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define tr(c, i) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c, x) ((c).find(x) != (c).end())
#define cpresent(c, x) (find(all(c), x) != (c).end())
#define REP(i, n) for(int i = 0; i < (n); i++)
#define REPD(i, n) for(int i = (n)-1; i >= 0; i--)
#define FOR(i, a, b) for(int i = (a); i <= (b); i++)
#define FORD(i, a, b) for(int i = (a); i >= (b); i--)
#define mp make_pair
#define CHECK(S, j) (S & (1 << j))
#define SET(S, j) (S |= (1 << j))
#define SETALL(S, j) (S = (1 << j)-1)
#define UNSET(S, j) (S &= ~(1 << j))
#define TOGGLE(S, j) (S ^= (1 << j))
#define LL long long
#define PI acos(-1)
template<class T>string tostring(T t){stringstream s;s<<t;return s.str();}

//GCJ Includes
#include <fstream>

int main() {
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.out");
    int t;
    fin >> t;
    REP(k, t){
        int a1, a2;
        int arr1[4][4], arr2[4][4];
        fin >> a1;
        REP(i, 4)
            REP(j, 4)
                fin >> arr1[i][j];
        fin >> a2;
        REP(i, 4)
            REP(j, 4)
                fin >> arr2[i][j];
        int ans = 0, match = 0;
        REP(i, 4){
            REP(j, 4){
                if(arr1[a1-1][i] == arr2[a2-1][j]){
                    match++;
                    ans = arr1[a1-1][i];
                }
            }
        }
        if(match == 1)
            fout << "Case #" << k+1 << ": " << ans << endl;
        else if(match == 0)
            fout << "Case #" << k+1 << ": " << "Volunteer cheated!" << endl;
        else fout << "Case #" << k+1 << ": " << "Bad magician!" << endl;
    }
    return 0;
}
