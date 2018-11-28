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

void Add(vector<bool>& v) {
    for (int i = v.size() - 1; i >= 0; --i) {
        if (!v[i]) {
            v[i] = true;
            break;
        }
        else {
            v[i] = false;
        }
    }
}
void Process(int n, int j, fstream &cout) {
    vector<bool> v(n / 2 - 1, false);
    for (int i = 0; i < j; ++i) {
        cout << '1';
        F2(i, v) {
            if (v[i])
            	cout << "11";
            else
                cout << "00";
        }
        cout << '1';
        
        for (int i = 2; i <= 10; ++i) {
            cout << ' ' << i + 1;
        }
        cout << endl;
        Add(v);
    }
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
        int n, j;
        cin >> n >> j;
        
        cout << "Case #" << i + 1 << ":" << endl;
        Process(n, j, cout);
    }
    return 0;
}