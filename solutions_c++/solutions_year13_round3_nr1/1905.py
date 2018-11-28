#include <cassert>
#include <iostream>
#include <map>
#include <string>
#include <utility>

using namespace std;

bool is_consonant(char c)
{
    if (c == 'a') return false;
    if (c == 'e') return false;
    if (c == 'i') return false;
    if (c == 'o') return false;
    if (c == 'u') return false;
    return true;
}

string name;
int n;
map<pair<int,int>, bool> cache;
int count;

bool solve_rec(int start, int len)
{
    if (len < n)
    {
        return 0;
    }
    pair<int, int> args = make_pair(start, len);
    auto it = cache.find(args);
    if (it != cache.end())
    {
        return (*it).second;
    }
    if (len == n)
    {
        for (int i = start; i < start+len; i++)
        {
            char c = name[i];
            if (!is_consonant(c))
            {
                cache[args] = false;
                return false;
            }
        }
        count++;
        cache[args] = true;
        return true;
    }
    bool sub_left  = solve_rec(start,   len-1);
    bool sub_right = solve_rec(start+1, len-1);
    bool result = sub_left || sub_right;
    if (result)
    {
        count++;
    }
    cache[args] = result;
    return result;
}

int solve()
{
    count = 0;
    cache.clear();
    solve_rec(0, name.size());
    return count;
}

int main()
{
    int T; cin >> T;
    for (int tt = 0; tt < T; tt++)
    {
        cin >> name >> n;
        cout << "Case #" << (tt+1) << ": " << solve() << endl;
    }
    return 0;
}

