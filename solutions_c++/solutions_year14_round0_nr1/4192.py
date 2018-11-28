#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>
#include <queue>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = ((long long)1 << 62) - 1;
const long double pi = acos(-1);

template <class T> T sqr (T x) {return x * x;}
template <class T> T abs (T x) {return x < 0 ? -x : x;}

bool key[2][20];
int a[4][4];

int main ()
{
//  ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int t;
    cin >> t;

    for (int tc = 0; tc < t; ++tc) {
        int row;

        for (int k = 0; k < 2; ++k) {
            for (int i = 1; i <= 16; ++i) {
                key[k][i] = false;
            }
        }

        for (int k = 0; k < 2; ++k) {
            cin >> row;
            row--;
            for (int i = 0; i < 4; ++i) {
                for (int j = 0; j < 4; ++j) {
                    cin >> a[i][j];
                }
            }

            for (int j = 0; j < 4; ++j) {
                key[k][a[row][j]] = true;
            }
        }

        int num = 0;
        int ind;

        for (int i = 1; i <= 16; ++i) {
            if (key[0][i] && key[1][i]) {
                num++;
                ind = i;
            }
        }

        printf ("Case #%d: ", tc + 1);
        if (num == 0) {
            cout << "Volunteer cheated!" << endl;
        } else if (num > 1) {
            cout << "Bad magician!" << endl;
        } else {
            cout << ind << endl;
        }
    }


	return 0;
}
