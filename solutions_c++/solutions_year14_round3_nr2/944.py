#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <tuple>
#include <utility>
#include <vector>

using namespace std;

#define REP(i,n) for(int i=0,nn=static_cast<int>(n);i<nn;i++)
#define REP_R(i,n) for(int i=static_cast<int>(n)-1;i>=0;i--)
#define ALL(v) v.begin(),v.end()
#define ALL_R(v) v.rbegin(),v.rend()

const long MOD = 1000000007;

void solve()
{
    int N; cin >> N;
    string cars[100];
    REP(i,N) { cin >> cars[i]; stringstream ss; ss << i; cars[i] += ss.str(); }
    sort(cars, cars+N);
    int count = 0;
    do
    {
        bool valid = true;
        set<char> chars;
        bool letters[26]; memset(letters, 0, sizeof letters);
        char prev = '-';
        REP(i,N)
        {
            REP(j, cars[i].size())
            {
                char c = cars[i][j];
                if (c >= '0' && c <= '9') continue;
                if (!letters[c-'a'])
                {
                    letters[c-'a'] = true;
                }
                else if (c != prev)
                {
                    valid = false;
                    goto jmp;
                }
                prev = c;
            }
        }
jmp:    if (valid)
        {
            count++;
        }
    } while (next_permutation(cars, cars+N));
    cout << count << endl;
}

int main()
{
    int T; cin >> T;
    REP(t, T)
    {
        cout << "Case #" << (t+1) << ": ";
        solve();
    }
    return 0;
}

