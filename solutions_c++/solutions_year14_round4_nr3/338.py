// <=================================================================>
//
//             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
//                     Version 2, December 2004
//
//  Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
//
//  Everyone is permitted to copy and distribute verbatim or modified
//  copies of this license document, and changing it is allowed as long
//  as the name is changed.
//
//             DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
//    TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
//
//   0. You just DO WHAT THE FUCK YOU WANT TO.
//
// <=================================================================>

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <queue>
#include <deque>
#include <sstream>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;

#ifdef moskupols
    #define debug(...) fprintf(stderr, __VA_ARGS__) // thank Skird it's friday!
#else
    #define debug(...) 42
#endif

#define timestamp(x) debug("["#x"]: %.3f\n", (double)clock() / CLOCKS_PER_SEC) // thank PavelKunyavskiy i am not pregnant!

#define hot(x) (x)
#define sweet(value) (value)
#define lovelyCute(nine) 9

#define ALL(v) (v).begin(), (v).end()

typedef long long int64;
typedef unsigned long long uint64;
typedef long double real;

// --- end of great templeat ---
//
//

const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, 1,  0,-1};

const int maxh = 505, maxw = 105;
const int maxv = maxh*maxw*2;
const int maxe = maxv*8;
bool abused[maxh][maxw];
int source, sink;
int w, h;

int head[maxv];
int ne[maxe], to[maxe], cap[maxe], f[maxe];
int esz = 0;

int used[maxv];
int q;

void addEdge(int a, int b)
{
    ne[esz] = head[a];
    to[esz] = b;
    cap[esz] = 1;
    f[esz] = 0;
    head[a] = esz++;

    ne[esz] = head[b];
    to[esz] = a;
    cap[esz] = 0;
    f[esz] = 0;
    head[b] = esz++;
}

#define id(x,y,t) (((x)*w+(y))*2+(t))

int dfs(int v)
{
    if (v == sink)
        return 1;
    if (used[v] == q)
        return 0;
    used[v] = q;
    for (int e = head[v]; e != -1; e = ne[e])
    {
        if (cap[e] <= f[e] || to[e] == source)
            continue;
        if (dfs(to[e]))
        {
            ++f[e];
            --f[e^1];
            return 1;
        }
    }
    return 0;
}

void solve()
{
    int b;
    cin >> w >> h >> b;
    memset(abused, 0, sizeof abused);
    for (int i = 0; i < b; ++i)
    {
        int x0, y0, x1, y1;
        cin >> x0 >> y0 >> x1 >> y1;
        for (int i = x0; i <= x1; ++i)
            for (int j = y0; j <= y1; ++j)
                abused[j][i] = true;
    }
    source = id(h, 0, 0);
    sink = source + 1;
    esz = 0;
    memset(head, -1, sizeof head);

    for (int i = 0; i < w; ++i)
        addEdge(source, id(0, i, 0));
    for (int i = 0; i < h; ++i)
        for (int j = 0; j < w; ++j)
        {
            if (abused[i][j])
                continue;
            addEdge(id(i, j, 0), id(i, j, 1));
            for (int k = 0; k < 4; ++k)
            {
                int x = i + dx[k], y = j + dy[k];
                if (x >= 0 && y >= 0 && x < h && y < w)
                    addEdge(id(i, j, 1), id(x, y, 0));
            }
        }
    for (int i = 0; i < w; ++i)
        addEdge(id(h-1, i, 1), sink);

    memset(used, -1, sizeof used);
    q = 0;
    while (dfs(source))
        ++q;
    cout << q << endl;
}

int main()
{
	cin.sync_with_stdio(false);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": ";
        solve();
    }

	timestamp(end);
	return 0;
}

