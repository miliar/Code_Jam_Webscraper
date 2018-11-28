#include <iostream>
#include <iomanip>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <bitset>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <cstring>
#include <fstream>
#include <functional>
#include <stack>
#include <complex>
#include <wchar.h>
#include <wctype.h>
#include <cmath>
#include <queue>
#include <ctime>
#include <unordered_set>
#include <numeric>
#include <bitset>
#include <cassert>


using namespace std;

template<typename T> T mabs(const T &a){ return a<0?-a:a;}
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<double, int> pdi;
typedef pair<double, double> pdd;

vector<string> split(char *str)
{
    vector<string> res;
    char *last = str;
    rep(i,0,strlen(str)+1)
    if (str[i]==0 || isspace(str[i]))
    {
        if (last != str + i)
        {
            str[i] =0;
            res.push_back(last);
        }
        last = str + i + 1;
    }
    return res;
}

char str[1000100];
void test(int testInd)
{
    int n;
    cin>>n;
    cin.get();
    vector<int> vec[200];
    map<string, int> mp;
    rep(i,0,n)
    {
        gets(str);
        auto v = split(str);
        rep(j,0,v.size())
        {
            int sz = mp.size();
            if (mp.find(v[j]) == mp.end())
                mp[v[j]] = sz;
            vec[i].push_back(mp[v[j]]);
        }
    }
    int res = 0;
    int used[2][10000] = {0};
    rep(j,0,vec[0].size())
        used[0][vec[0][j]]++;
    rep(j,0,vec[1].size())
    {
        if (used[0][vec[1][j]] > 0 && used[1][vec[1][j]] == 0)
            ++res;
        used[1][vec[1][j]]++;
    }
    int add = 1e9;
    rep(i,0,1<<(n-2))
    {
        int curr = 0;
        rep(j,0,n-2)
        {
            int put = (i>>j)&1;
            int ask = put^1;
            rep(k,0,vec[j+2].size())
            {
                auto &s = vec[j+2][k];
                if (used[ask][s] > 0 && used[put][s] == 0)
                    ++curr;
                used[put][s]++;
            }
        }
        rep(j,0,n-2)
        {
            int put = (i>>j)&1;
            int ask = put^1;
            rep(k,0,vec[j+2].size())
            {
                auto &s = vec[j+2][k];
                used[put][s]--;
            }
        }
        add = min(add, curr);
    }
    res += add;
    cout<<res<<endl;
}

void run()
{
    int t;
    cin>>t;
    rep(i,0,t)
    {
        printf("Case #%d: ", i+1);
        fprintf(stderr,"%d/%d\n", i+1, t);
        test(i);
    }
}

#define prob "C-small-attempt1"



int main()
{
#ifdef _MONYURA_
#ifdef prob
    freopen("../" prob ".in","r",stdin);
    freopen("../" prob ".out","w",stdout);
#else
    freopen("../test.in","r",stdin);
    freopen("../test.out","w",stdout);
    time_t st=clock();
#endif
#else
#endif
    run();
#ifdef _MONYURA_
#ifndef prob
    printf( "\n=============\n");
    printf("Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
#endif
#endif
    
    return 0;
}