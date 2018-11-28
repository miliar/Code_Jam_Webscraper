#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)

#define forall(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++

typedef long long tint;

const tint MOD = 1000000007;

vector<string> s;
vector<vector<int> > parti;

int lcp(const string &a, const string &b)
{
    int ret = 0;
    while (ret < (int)a.size() && ret < (int)b.size() && a[ret] == b[ret]) ret++;
    return ret;
}

const string vacia;

int trieNodes(const vector<int> &v)
{
    // vs esta ordenado!
    int ret = 1;
    
    const string* last = &vacia;
    forn(i, v.size())
    {
        const string &current = s[v[i]];
        ret += current.size() - lcp(current, *last);
        last = &current;
    }
    return ret;
}

tint maxNodes, ways;

int N;

void backtrack(int M)
{
    if (M == 0)
    {
        forn(i,N) if (parti[i].empty()) return;
        tint nodes = 0;
        forn(i,N) nodes += trieNodes(parti[i]);
        if (nodes > maxNodes)
        {
            maxNodes = nodes;
            ways = 1;
        }
        else if (nodes == maxNodes)
            ways++;
    }
    else
    {
        M--;
        forn(i,N)
        {
            parti[i].push_back(M);
            backtrack(M);
            parti[i].pop_back();
        }
    }
}

int main()
{
    int TT; scanf("%d", &TT);
    forn(tt,TT)
    {
        int M;
        cin >> M >> N;
        s = vector<string>(M);
        forn(i,M) cin >> s[i];
        sort(s.rbegin(), s.rend());
        maxNodes = 0; ways = 0;
        parti = vector<vector<int> >(N, vector<int>());
        backtrack(M);
        printf("Case #%d: %lld %lld\n" , tt+1, maxNodes, ways);
    }
    return 0;
}

