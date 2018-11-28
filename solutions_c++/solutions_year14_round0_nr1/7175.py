#include <iostream>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <deque>
#include <queue>
#include <iomanip>
#include <algorithm>
#include <vector>

#define ull unsigned long long
#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define iter iterator

using namespace std;

void Solve()
{
    int n, m, a;
    set <int> A, B;
    cin >> n;
    for (int i = 1; i <= 4; ++i)
        for (int j = 1; j <= 4; ++j)
        {
            cin >> a;
            if (i == n)
                A.insert(a);
        }
    cin >> m;
    for (int i = 1; i <= 4; ++i)
        for (int j = 1; j <= 4; ++j)
        {
            cin >> a;
            if (i == m)
                if (A.find(a) != A.end())
                    B.insert(a);
        }
    if (B.size() == 0)
        cout << "Volunteer cheated!";
    else if (B.size() == 1)
        cout << *B.begin();
    else
        cout << "Bad magician!";
}

int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    freopen("ans.txt", "w", stdout);

    ios_base::sync_with_stdio(false);
    int NumOfTests;
    cin >> NumOfTests;
    for (int i = 1; i <= NumOfTests; ++i)
    {
        cout << "Case #" << i << ": ";
        Solve();
        cout << endl;
    }
}
