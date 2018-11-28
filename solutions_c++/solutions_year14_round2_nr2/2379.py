//--CodeJam-A//
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

int main() {
    ifstream fin("/Users/usamaelnily/Desktop/in.txt");
    ofstream fout("/Users/usamaelnily/Desktop/out.txt");
    int cs, t;
    fin >> cs;
    t = cs;
    while(cs--) {
        int a, b, k, ans = 0;
        fin >> a >> b >> k;
        for(int i = 0; i < a; i++) {
            for(int j = 0; j < b; j++) {
                if((i&j) < k)
                    ans++;
            }
        }
        fout << "Case #" << t - cs << ": " << ans << endl;
    }
    return 0;
}