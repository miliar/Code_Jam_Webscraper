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

inline double getMinTime(double C, double F, double X) {
    double perSecond = 2;
    double totalTime = 0;
    while(1) {
        double timeTillC = C / perSecond + X / (perSecond + F);
        double timeTillX = X / perSecond;
        if(timeTillX <= timeTillC || fabs(timeTillC - timeTillX) == 0.000000001) {
            totalTime += timeTillX;
            return totalTime;
        }
        totalTime += C / perSecond;
        perSecond += F;
    }
}

int main() {
    cin.sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);
    #endif
    int T;
    cin >> T;
    for(int test = 1 ; test <= T ; ++ test) {
        double C, F, X;
        cin >> C >> F >> X;
        cout << "Case #" << test << ": " << fixed << setprecision(7) << getMinTime(C, F, X) << '\n';
    }
    fin.close();
    fout.close();
    return 0;
}
