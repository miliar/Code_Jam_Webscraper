#include "vector"
#include "string"
#include "set"
#include "map"
#include "sstream"
#include "algorithm"
#include "cmath"
#include "cassert"
#include "iostream"
#include "numeric"
#include "fstream"
#include "queue"
#include <functional>
#include <climits>
#include <cstring>
#include <list>
#include <iomanip>

using namespace  std;

#define int64 long long
#define F(vec, index) for (int index=0; index  < vec.size(); ++index)
#define F2(index, vec) for (int index=0; index  < vec.size(); ++index)
#define F3(index, from, vec) for (int indexfrom + 1; index  < vec.size(); ++index)

int Process(int64 n) {
    int64 currN = 0;
    vector<int> was(10, 0);
    while (true) {
        currN += n;
        
        int64 divN = currN;
        while (divN != 0) {
            was[divN % 10] = 1;
            divN /= 10;
        }
        int a = accumulate(was.begin(), was.end(), 0);
        if (a == 10) {
            return currN;
        }
        
    }
}
/*
15
1000000
999999
999998
999997
999996
999995
999994
999993
999992
999991
999990
100000
500000
100001
111111
*/

int main(int argc, char* argv[])
{
    std::ios::sync_with_stdio(false);
    fstream cout("/Users/a-voronin/xcode/codeJam.txt",fstream::out);
    //cout << "test" << endl;
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        std::cout << i << endl;
        int n;
        cin >> n;
        if (n == 0) {
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        int res = Process(n);
        cout << "Case #" << i + 1 << ": " << res << endl;
    }
    return 0;
}