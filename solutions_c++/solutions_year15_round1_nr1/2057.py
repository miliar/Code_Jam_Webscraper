#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <iomanip>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int>> vpii;
typedef vector<vector<int>> vvin;
typedef unsigned long long ULL;

int arr[1001];
int main (int argc, char *args[]) {

    int N; cin >> N;
    for (int zz = 1; zz <= N; zz++) {
        int x; cin >> x;
        REP (j, x) cin >> arr[j];

        ULL a = 0;
        int md = -1;
        for (int i = 1; i < x; i++) {
            if (arr[i] < arr[i-1]) {
                a += arr[i-1] - arr[i];
                md = max(md, arr[i-1]-arr[i]);
            }
        }
        ULL b = 0;
        for (int i = 0; i < x-1; i++) {
            if (arr[i] - md < 0) b += arr[i];
            else b += md;
        }
        if (md < 0) b = 0;
        cout << "Case #" << zz << ": " << a << " " << b << endl;
    }
    return 0;
}


