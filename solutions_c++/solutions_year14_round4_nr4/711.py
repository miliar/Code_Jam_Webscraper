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
#include <numeric>
#include <bitset>


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

vector<string> vec[4];
string str[8];

struct node
{
    map<char,int> mp;
} E[100100];
int epos;

void addWord(string str)
{
    int st = 0;
    rep(i,0, str.size())
    {
        if (E[st].mp.find(str[i]) == E[st].mp.end())
            E[st].mp[str[i]] = epos++;
        st = E[st].mp[str[i]];
    }
}

int getCnt(vector<string> &vec)
{
    epos = 1;
    int res = 1;
    rep(i,0,vec.size())
        addWord(vec[i]);
    int ans = epos;
    rep(i,0,epos)
    E[i].mp.clear();
    return ans;
}

int mx = -1;
int cnt  = 0;

void rec(int pos, int n, int s)
{
    if (pos == n)
    {
        int curr = 0;
        rep(i,0,s)
        {
            if (vec[i].empty())
                return;
            curr += getCnt(vec[i]);
        }
        if (curr > mx)
        {
            mx = curr;
            cnt = 0;
        }
        if (curr == mx)
            ++cnt;
    }
    else
    {
        rep(k,0,s)
        {
            vec[k].push_back(str[pos]);
            rec(pos+1,n,s);
            vec[k].pop_back();
        }
    }
}

void test()
{
    mx = -1;
    cnt = 0;
    char s[100100];
    int n,t;
    cin>>n>>t;
    rep(i,0,n)
    {
        scanf("%s",s);
        str[i] = s;
    }
    rec(0, n, t);
    printf("%d %d\n", mx, cnt);
}

void run()
{
    int t;
    cin>>t;
    rep(i,0,t)
    {
        cerr<<"test "<<i+1<<endl;
        printf("Case #%d: ", i+1);
        test();
    }
}


#define prob "D-small-attempt1"


int main()
{
#ifdef _MONYURA_
    #ifdef prob
        freopen(prob".in","r",stdin);
        freopen(prob".out","w",stdout);
    #else
        freopen("test.in","r",stdin);
        freopen("test.out","w",stdout);
        time_t st=clock();
    #endif
#else
    #ifdef prob
        freopen(prob".in","r",stdin);
        freopen(prob".out","w",stdout);
    #endif
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
