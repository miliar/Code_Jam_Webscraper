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
    freopen("in", "r", stdin); freopen("out", "w", stdout);
    int t; cin >> t;
    string line;
    getline(cin,line);
    for (int tt = 1; tt <= t; tt++)
    {
        cerr << "Executing Case #" << tt << "\n";
        int cur = 0;
        getline(cin, line);
        cerr << line.length() << endl;
        cerr << line[0] << endl;
        for (int i = 1; i < line.length()-1; i++){
            if(line[i] != line[i-1]) cur++;
        }
        if(line[0] == '-' ^ (cur % 2)) cur++;
        cout << "Case #" << tt << ": " << cur << endl;
    }
    return 0;
}
