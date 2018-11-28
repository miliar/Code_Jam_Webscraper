#include <iostream>
#include <list>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <cassert>
#include <vector>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <stack>
#include <queue>
#include <deque>
#include <utility>
#include <set>
#include <unordered_set>

using namespace std;

string s;

bool is_valid()
{
        for(char c : s)
                if(c == '-')
                        return false;
        return true;
}

void invert(int index)
{
        for(int i = 0;i < index;i++)
                s[i] = s[i] == '+' ? '-' : '+';
}

int solve()
{
        int c = 0;
        char cur = s.front();
        int i,n;
        i = 0;
        n = s.length();
        while(i < n)
        {
                if(s[i] != cur)
                {
                        invert(i);
                        cur = cur == '+' ? '-' : '+';
                        c++;
                }
                i++;
        }
        return c + !is_valid();
}

int main()
{
        ios_base::sync_with_stdio(false);
        int t;
        cin >> t;
        for(int i = 1;i <= t;i++)
        {
                cin >> s;
                cout << "Case #" << i << ": " << solve() << endl;
        }
        return 0;
}
