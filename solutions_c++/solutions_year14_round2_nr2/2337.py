#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define RANGE(i,b,e) for(int (i)=(b);(i)<(int)(e);(i)++)
#define CRANGE(i,b,e) for(int (i)=(b);(i)<=(int)(e);(i)++)
#define RRANGE(i,b,e) for(int (i)=(b);(i)>=(int)(e);(i)--)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define PI 3.1415926535897932384626433832795
#define INF 0x7FFFFFFF

int T;
int A, B, K;

int main(int argc, char **argv)
{
    cin >> T;
    for (int t = 0;t < T;t++) {
        int cnt = 0;
        cin >> A >> B >> K;
        REP(a, A) {
            REP(b, B) {
                if ((a & b) < K) {
                    cnt++;
                }
            }
        }

        //  Output.
        cout << "Case #" << t + 1 << ": ";
        cout << cnt << endl;
    }

    return 0;
}
