#include <vector> // headers {{{
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <ctime>

#define DEBUG(x) cout << #x << ": " << x << "\n"
using namespace std; // }}}

set<int> readPart(ifstream& cin)
{
    int x0;
    cin >> x0;
    set<int> S0;
    for (int i = 1; i <= 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            int cur;
            cin >> cur;
            if (i == x0)
                S0.insert(cur);
        }
    }
    return S0;
}

string result(ifstream& cin)
{
    set<int> S0 = readPart(cin);
    set<int> S1 = readPart(cin);
    set<int> intrs;
    set_intersection(S0.begin(), S0.end(), S1.begin(), S1.end(), inserter(intrs, intrs.begin()));
    if (intrs.size() == 0)
        return "Volunteer cheated!";
    if (intrs.size() > 1)
        return "Bad magician!";
    stringstream ss0;
    ss0 << *intrs.begin();
    return ss0.str();
}

int main()
{
    time_t start, end;
    time(&start);
    
    ifstream cin("test.in");
    ofstream cout("test.out");
    //cout.precision(6);
    //cout.setf(ios::fixed,ios::floatfield);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": " << result(cin) << endl;
        time(&end);
        ::cout << i << " " << difftime(end, start) << endl;
    }

    return 0;
}
