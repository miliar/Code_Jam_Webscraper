#include <iostream>
#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <stdint.h>

#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <bitset>
#include <deque>
#include <list>
#include <stack>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define all(v) (v).begin(), (v).end()
#define foreach(it, v) for(__typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define sz(v) int((v).size())


void solve()
{
    int files_count, capacity;
    cin >> files_count >> capacity;
    vector < int > files(files_count);
    for(int i = 0; i < files_count; i++)
        cin >> files[i];
    int result = 0;
    vector < bool > used(files_count, false);
    for(int i = 0; i < files_count; i++)
    {
        if(!used[i])
        {
            int best = -1;
            for(int j = 0; j < files_count; j++)
            {
                if(i != j && !used[j])
                {
                    if(files[i] + files[j] <= capacity)
                    {
                        if(best == -1 || files[j] > files[best])
                        {
                            best = j;
                        }
                    }
                }
            }
            ++result;
            used[i] = true;
            if(best != -1)
                used[best] = true;
        }
    }
    cout << result << endl;
}

int main()
{
    int tests;
    cin >> tests;
    for(int test = 1; test <= tests; test++)
    {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}