#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <iomanip>
#include <set>

using namespace std;

typedef long double ld;

multiset<string> s;
string voc;
void perebor(string cur, int lft)
{
    if(lft == 0)
    {
        s.insert(cur);
    }
    else
    {
        for(int i = 0; i < voc.length(); ++i)
        {
            perebor(cur + voc[i], lft - 1);
        }
    }
}

int k, l, ss;
string key;

ld brute()
{
    s.clear();
    perebor("", ss);

    ld sm = 0;
    ld mx = 0;
    ld cnt = s.size();
//        vector<ld> cnt;
    for(set<string>::iterator it = s.begin(); it != s.end(); ++it)
    {
//            cout << " >> " << (*it) << endl;
        ld q = 0;
        for(int i = l-1; i < ss; ++i)
        {
            if((*it).substr(i - l + 1, l) == key)
                q += 1;
        }
//            cnt.push_back(cnt);
        mx = max(mx, q);
        sm += q;
    }

    ld ans = mx - sm / cnt;
    return ans;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);

    int TTT;
    cin >> TTT;
    for(int T = 1; T <= TTT; ++T)
    {
        cin >> k >> l >> ss;
        cin >> voc;
        cin >> key;

        ld ans = brute();

        cout << "Case #" << T << ": ";
        cout << fixed << setprecision(7) << ans << endl;
    }

    return 0;
}
