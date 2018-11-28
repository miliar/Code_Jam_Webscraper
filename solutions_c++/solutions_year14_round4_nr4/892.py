#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdlib>
#include <list>
#include <set>
#include <ctime>
#include <list>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define vi vector<int>
#define vd vector<double>
#define pii pair<int,int>
#define pdd pair<double,double>
#define ll long long
#define INF (1<<30)
using namespace std;

int N, M;
string S[10];
int w[10];
set<string> U;
vector<string> v[10];
int best = 0, times = 0;

void check()
{
    int i, j, k, l;
    for(i = 0; i < N; ++i) v[i].clear();
    for(i = 0; i < M; ++i)
    {
        v[w[i]].pb(S[i]);
    }
    for(i = 0; i < N; ++i)
    {
        if(v[i].size() == 0) return;
    }
    int cr = 0;
    for(i = 0; i < N; ++i)
    {
        U.clear();
        for(j = 0; j < v[i].size(); ++j)
        {
            string s = "";
            for(k = 0; k < v[i][j].length(); ++k)
            {
                U.insert(s);
                s.pb(v[i][j][k]);
            }
            U.insert(s);
        }
        cr += U.size();
    }
    if(cr > best)
    {
        best = cr;
        times = 1;
    }
    else if(cr == best) ++times;
}

void go(int ind)
{
    if(ind == M)
    {
        check();
        return;
    }
    for(int i = 0; i < N; ++i)
    {
        w[ind] = i;
        go(ind + 1);
    }
}

void solve_case(int case_id)
{
    printf("Case #%d: ", case_id);
    int i, j;
    cin >> M >> N;
    for(i = 0; i < M; ++i) cin >> S[i];
    best = 0; times = 0;
    go(0);
    cout << best << ' ' << times << '\n';
}

int main()
{
    int i, t;
    scanf("%d", &t);
    for(i = 1; i <= t; ++i) solve_case(i);
    return 0;
}
