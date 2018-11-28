#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <map>
#include <fstream>
#include <sstream>
#include <math.h>
#include <stack>
#include <string.h>
using namespace std;

#define FOR(i, a, b) for(int i=a; i<b; i++)
#define FORE(i, a, b) for(int i=a; i<=b; i++)
#define ll long long
#define mp make_pair
#define pii pair<int, int>
#define pll pair<long, long>
#define PI 3.14159265359
#define mod 1000000007

#define maxN 2500

int A[4][4], B[4][4], a, b;

int main()
{
    ifstream ifs("a.in");
    ofstream ofs("a.out");
    int T;
    ifs >> T;
    FOR(awt, 0, T) {
        ifs >> a;
        FOR(i, 0, 4)
            FOR(j, 0, 4) ifs >> A[i][j];
        ifs >> b;
        FOR(i, 0, 4)
            FOR(j, 0, 4) ifs >> B[i][j];

        int p[4];
        FOR(i, 0, 4) p[i] = A[a-1][i];

        int r=0, l;
        FOR(i, 0, 4) 
        FOR(j, 0, 4) {
            if(B[b-1][i] == p[j]) {
                r++;
                l = p[j];
            }
        }
        switch(r) {
            case 0:
            ofs << "Case #" << awt+1 << ": Volunteer cheated!" << endl;
            break;

            case 1:
            ofs << "Case #" << awt+1 << ": " << l << endl;
            break;

            default:
            ofs << "Case #" << awt+1 << ": Bad magician!" << endl;
            break;
        }




    }
}
