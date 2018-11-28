#define _USE_MATH_DEFINES
#include <iostream>
#include <utility>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cmath>
#include <queue>
#include <functional>
#include <cstdio>
#include <cassert>
#include <stack>
#include <sstream>

#define mp make_pair
#define mt(x,y,z) mp((x), mp((y), (z)))
#define ZERO(x) memset((x), 0, sizeof(x))
#define NEGATE(x) memset((x), 255, sizeof(x))
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;

// globals starts here

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while (getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}


std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, elems);
    return elems;
}

const int MAX_N = 205;
const int MAX_W = 3000;
set<int> sent[MAX_N];
vector<int> wos[MAX_W];
int id;
int n;

int intes(int mask)
{
    int cnt = 0;
    for (int j = 0; j < id; ++j)
    {
        int en = 0;
        int fr = 0;
        for (int se : wos[j])
        {
            if (se == 0)
            {
                ++en;
            }
            else if (se == 1)
            {
                ++fr;
            }
            else if ((1 << (se - 2)) & mask)
            {
                ++en;
            }
            else
            {
                ++fr;
            }
        }

        if (en > 0 && fr > 0)
        {
            ++cnt;
        }
    }
    return cnt;
}

int main()
{
#ifdef DEBUGAGA
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);	
#elif defined(CONTEST)
    freopen(CONTEST ".in", "r", stdin);
    freopen(CONTEST ".out", "w", stdout);
#endif

    int tests;
    cin >> tests;
    for (int tc = 1; tc <= tests; ++tc)
    {
        for (int i = 0; i < MAX_N; ++i)
        {
            sent[i].clear();
        }

        map<string, int> mapa;
        id = 0;
        cin >> n;
        string line;
        getline(cin, line);
        for (int i = 0; i < n; ++i)
        {
            getline(cin, line);
            vector<string> words = split(line, ' ');
            for (auto& word : words)
            {
                if (mapa.count(word) == 0)
                {
                    mapa.insert(mp(word, id++));
                }

                sent[i].insert(mapa[word]);
            }
        }

        for (int i = 0; i < id; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (sent[j].count(i) > 0)
                {
                    wos[i].push_back(j);
                }
            }
        }

        int rest = n - 2;
        int masks = 1 << rest;
        int mina = 10000000;
        for (int i = 0; i < masks; ++i)
        {
            int cur = intes(i);
            mina = min(mina, cur);
        }

        printf("Case #%d: %d\n", tc, mina);

        for (int i = 0; i < id; ++i)
        {
            wos[i].clear();
        }
    }

    return 0;
}