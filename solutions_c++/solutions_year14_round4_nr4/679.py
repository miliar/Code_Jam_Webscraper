#pragma comment(linker, "/STACK:65000000")
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cmath>
#include<complex>
#include<ctime>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<int> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
//#define LL "%I64d"
#define RLL(x) scanf(LL,&(x))

int n,m;

string mas[8];

vector<string> vs[4];

int g[100][26];

int res = 0;
int way = 0;

int calc(vector<string> &v)
{
    if(v.size() == 0)
        return 0;
    int answ = 1;
    memset(g, -1, sizeof(g));
    for(int i = 0; i < v.size(); ++i)
    {
        int cur = 0;
        for(int j = 0; j < v[i].size(); ++j)
        {
            if(g[cur][v[i][j] - 'A'] == -1)
                g[cur][v[i][j] - 'A'] = answ++;
            cur = g[cur][v[i][j] - 'A'];
        }
    }
    return answ;
}

void obx(int cur)
{
    if(cur == m)
    {
        int answ = 0;
        for(int i=0; i<n; ++i)
            answ += calc(vs[i]);
        if(res < answ)
        {
            res = answ;
            way = 1;
        }
        else
            if(res == answ)
                ++way;
        return;
    }
    for(int i = 0; i < n; ++i)
    {
        vs[i].push_back(mas[cur]);
        obx(cur+1);
        vs[i].pop_back();
    }
}

void test(int T)
{
    cin>>m>>n;
    res = 0;
    way = 0;
    for(int i=0; i<m; ++i)
        cin>>mas[i];
    obx(0);
    printf("Case #%d: %d %d\n", T, res, way);
}

int main(int argc, const char * argv[])
{
    
    freopen("/Users/olpet/Downloads/GCJ/d.in", "r", stdin);
    freopen("/Users/olpet/Downloads/GCJ/d.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 0; t < T; ++t)
        test(t+1);
    return 0;
}