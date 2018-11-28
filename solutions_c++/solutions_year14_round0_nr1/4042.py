#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <complex>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <cfloat>
#include <ctime>

using namespace std;

#define DBG(fmt, ...) fprintf(stderr, fmt, __VA_ARGS__);
#define DUMP(val) cerr << #val << " : " << (val) << endl

#define REP(a,b) for(a = 0; a < b; a++)
#define FOR(a,b,c) for(a = b; a < c; a++)
#define FOREACH(it, c) for (__typeof__((c).begin()) it=(c).begin(); it != (c).end(); ++it)

#define PUSH(e) push_back(e)
#define POP(e) pop_back(e)
#define MP(a,b) make_pair(a,b)
#define ALL(a) (a).begin(),(a).end()
#define RALL(a) (a).rbegin(),(a).rend()
#define SORT(a) sort((a).begin(),(b).end())
#define FILL(a,b) fill((a).begin(),(a).end(),b)

typedef pair<int,int> point;
#define F first
#define S second

typedef signed char int8_t;
typedef unsigned char uint8_t;
typedef signed short int16_t;
typedef unsigned short uint16_t;
typedef signed int int32_t;
typedef unsigned int uint32_t;



int main()
{
    int N;
    int A;
    int c[4][4];
    bool flags[16];
    
    cin >> N;
    for (int n = 0; n < N; n++) {
        cin >> A;
        A = A-1;
        for (int i = 0; i < 4; ++i) {
            cin>>c[i][0]>>c[i][1]>>c[i][2]>>c[i][3];
        }
        memset(flags, 0, sizeof(flags));
        for(int i = 0; i < 4; ++i) {
            flags[c[A][i]-1] = true;
        }
        cin >> A;
        A = A-1;
        for (int i = 0; i < 4; ++i) {
            cin>>c[i][0]>>c[i][1]>>c[i][2]>>c[i][3];
        }
        int count = 0;
        int num = 0;
        for(int i = 0; i < 4; ++i) {
            if(flags[c[A][i]-1]) {
                count++;
                num = c[A][i];
            }
        }
        cout << "Case #" << (n+1) << ": ";
        if(count == 0) {
            cout << "Volunteer cheated!" << endl;
        } else if(count != 1) {
            cout << "Bad magician!" << endl;
        } else {
            cout << num << endl;
        }
    }
    
    return 0;
}

