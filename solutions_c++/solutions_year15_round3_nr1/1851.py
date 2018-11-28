#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>

#define INF 1000000000

using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;
typedef pair<ll, ii> iii;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;

int main() {
	int nCases;
	cin >> nCases;
	for (int cnum = 1; cnum <= nCases; cnum++) {
        int R,C,W;
        cin >> R >> C >> W;
        if (W == 1)
        {
            cout << "Case #" << cnum << ": " << R*C << endl;
        }
        else
        {
            int shots = C / W;
            if (C % W != 0)
            {
                shots++;
            }
            shots *= R;
            shots += W-1;
            cout << "Case #" << cnum << ": " << shots << endl;
        }
	}
}
