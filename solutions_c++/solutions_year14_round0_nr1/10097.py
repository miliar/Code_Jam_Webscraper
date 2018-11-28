#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VII;
 
#define FOR(i, a, b) for(i = (a); i < (b); ++i)
#define SZ(a) int((a).size())
#define PB push_back
#define ALL(c) (c).begin(),(c).end()
#define SORT(c) sort(ALL(c))
#define COMMON(a,b) SORT(a), SORT(b), a.erase(set_intersection(ALL(a),ALL(b),a.begin()),a.end())

int readInt() { int n; if ( scanf("%d", &n) != 1 ) throw("invalid input"); return n; }

int main() {    
    // ./solution < input_file | tee output_file
    int T = readInt(), r1 = 0, r2 = 0, i = 0, j = 0;
    VII vIndex;
    vIndex.PB({-1, -1});
    vIndex.PB({0, 4});
    vIndex.PB({4, 8});
    vIndex.PB({8, 12});
    vIndex.PB({12, 16});
    FOR(i, 0, T) {
        r1 = readInt();
        VI v1, v2;
        FOR(j, 0, 16) v1.PB(readInt());
        r2 = readInt();
        FOR(j, 0, 16) v2.PB(readInt());
        VI a(v1.begin()+vIndex[r1][0], v1.begin()+vIndex[r1][1]);
        VI b(v2.begin()+vIndex[r2][0], v2.begin()+vIndex[r2][1]);
        COMMON(a, b);
        if ( SZ(a) == 0 ) cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
        else if ( SZ(a) > 1 ) cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
        else if ( SZ(a) == 1 ) cout << "Case #" << i+1 << ": " << a[0] << endl;
        else if ( SZ(b) == 1 ) cout << "Case #" << i+1 << ": " << b[0] << endl;
    }    
    return 0;
}