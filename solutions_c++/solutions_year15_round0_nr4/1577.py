#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>

typedef unsigned long long int ulld;
using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<bool> vb;

int main ()
{
    int t, caso = 1;
    cin >> t;
    while(t--){
        int x, r, c;
        cin >> x >> r >> c;
        if((r % x == 0 || c % x == 0) && (r * c ) >= (x * (x-1)))
            cout << "Case #" << caso++ << ": GABRIEL\n";
        else
            cout << "Case #" << caso++ << ": RICHARD\n";
    }
    return 0;
}