#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>
#include <cctype>

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;

template <class T> inline T sqr(const T& a) { return a * a; }
template <class T> inline void updMin(T& a, const T& b) { if (b < a) a = b; }
template <class T> inline void updMax(T& a, const T& b) { if (b > a) a = b; }




int n;
vector < vector<int> > words;
unordered_map <string, int> strIndex;
int maxIndex;


int getIndex(const string& word)
{
    if (strIndex.count(word) > 0)
        return strIndex[word];
    else
        return strIndex[word] = (++maxIndex);
}

void update(int& v, int x)
{
    if (v == -1)
        v = x;
    else
    {
        if (v != x)
            v = 2;
    }
}


void solution()
{
    words.clear();
    strIndex.clear();
    maxIndex = 0;

    string buf;

    cin >> n;
    getline(cin, buf);
    for (int i = 0; i < n; ++i)
    {
        getline(cin, buf);
        stringstream ss(buf);
        string word;
        words.push_back( vector<int> () );
        while (ss >> word)
        {
            words.back().push_back(getIndex(word));
        }
    }

    vector <int> a(maxIndex);

    uint upperMask = (1 << (n - 2));
    int ans = maxIndex + 100;
    for (uint mask = 0; mask < upperMask; ++mask)
    {

        a.assign(maxIndex, -1);
        for (int i = 0; i < words[0].size(); ++i)
            update(a[ words[0][i] - 1 ], 0);
        for (int i = 0; i < words[1].size(); ++i)
            update(a[ words[1][i] - 1 ], 1);

        for (int j = 2; j < n; ++j)
        {
            int t = (mask & (1 << (j - 2))) ? 1 : 0;
            for (int i = 0; i < words[j].size(); ++i)
            {
                update(a[ words[j][i] - 1], t);
            }
        }

        int cnt = 0;
        for (int i = 0; i < maxIndex; ++i)
        {
            if (a[i] == 2)
                ++cnt;
        }
        updMin(ans, cnt);
    }
    cout << ans;
}



int main()
{
    //freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    ios::sync_with_stdio(false);


    int nTests;
    cin >> nTests;
    for (int test = 1; test <= nTests; ++test)
    {
        cout << "Case #" << test << ": ";
        solution();
        cout << "\n";
    }



    return 0;
}
