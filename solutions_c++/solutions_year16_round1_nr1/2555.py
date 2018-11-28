#include <cstring>
#include <cmath>
#include <climits>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <string>
#include <iostream>
#include <algorithm>
#include <functional>
#include <utility>
using namespace std;
using ll = long long;
using ull = unsigned long long;

void solve()
{
    string str; cin >> str;
    deque<char> solution;

    for(char c : str)
    {
        if(c >= solution[0])
            solution.push_front(c);
        else
            solution.push_back(c);
    }
    for(char c : solution)
        cout << c;

}

int main()
{
    cout.precision(8);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }
    return 0;
}

