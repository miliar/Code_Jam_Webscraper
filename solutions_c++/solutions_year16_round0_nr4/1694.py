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
/*
5
-
-+
+-
+++
--+-
+++++++-
++++--++-
 */


void Process(int K, int C, int S, fstream &cout) {
//K = 3, C = 3
// 000
// 000000000
// 000000000000000000000000000
// 100
// 111 100 100
// 111 111 111 111 100 100 111 100 100
    
// 1000
// 1111 1000 1000 1000
// 1111 1111 1111 1111 1111 1000 1000 1000 1111 1000 1000 1000 1111 1000 1000 1000
    
// 0010
// 0010 0010 1111 0010
// 0010 0010 1111 0010 0010 0010 1111 0010 1111 1111 1111 1111 0010 0010 1111 0010
    
// 0001
// 0001 0001 0001 1111
// 0001 0001 0001 1111 0001 0001 0001 1111 0001 0001 0001 1111 1111 1111 1111 1111
    if (K == 1) {
       cout << ' ' << 1;
       return;
    }
    if (C == 1) {
        for (int i = 1; i <= K; ++i) {
            cout << ' ' << i;
            
        }
        return;
    }
    for (int i = 2; i <= K; ++i) {
        cout << ' ' << i;
        
    }
    return;
    
    
}


int main(int argc, char* argv[])
{
    std::ios::sync_with_stdio(false);
    fstream cout("/Users/a-voronin/xcode/codeJam.txt",fstream::out);
    fstream cin("/Users/a-voronin/xcode/codeJamInput.txt",fstream::in);
    
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        std::cout << i << endl;
        int K, C, S;
        cin >> K >> C >> S;
        cout << "Case #" << i + 1 << ":";
        Process(K, C, S, cout);
        cout << endl;
    }
    return 0;
}