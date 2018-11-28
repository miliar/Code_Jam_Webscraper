#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

#undef int
int main()
{
#define int long long
    freopen("in", "r", stdin); freopen("out","w",stdout);
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cerr << "Executing Case #" << tt << "\n";
        int n; cin >> n;
        if (n == 0){
            cout << "Case #" << tt << ": INSOMNIA\n";
            continue;
        }
        bool present[10];
        for (int i = 0; i < 10; i++) present[i] = false;
        int cur = 0, m =0;
        while(cur < 10){
            m += n;
            int m1 = m;
            while(m1 > 0){
                int d = m1 % 10;
                if(!present[d]) present[d] = true, cur++;
                m1 = m1/10;
            }
        }
        cout << "Case #" << tt << ": " << m << endl;
    }
    return 0;
}
