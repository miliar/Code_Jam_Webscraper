#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <algorithm>
#define pb push_back
using namespace std;

int A[4][4], B[4][4];

void solve(int tc)
{
    cout << "Case #" << tc << ": ";
    int i, j, r1, r2;
    cin >> r1;
    for(i = 0; i < 4; ++i)
        for(j = 0; j < 4; ++j) cin >> A[i][j];
    cin >> r2;
    for(i = 0; i < 4; ++i)
        for(j = 0; j < 4; ++j) cin >> B[i][j];
    int sol = -1;
    for(i = 0; i < 4; ++i)
    {
        for(j = 0; j < 4; ++j)
        {
            if(A[r1 - 1][i] == B[r2 - 1][j])
            {
                if(sol != -1)
                {
                    cout << "Bad magician!\n";
                    return;
                }
                sol = A[r1 - 1][i];
            }
        }
    }
    if(sol == -1) cout << "Volunteer cheated!\n";
    else cout << sol << '\n';
}

map<char, char> R;

int main()
{
    int tc, t;
    cin >> t;
    for(tc = 1; tc <= t; ++tc) solve(tc);
}
