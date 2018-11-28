#include <string>
#include <iostream>
#include <vector>
#include <utility>
#include <cstdio>
#include <sstream>
#include <cmath>
using namespace std;

long long E, R;
int N;
vector<long long> v;

void init()
{
    cin >> E >> R >> N;
    v.resize(N);
    for (int i = 0; i < N; ++i) cin >> v[i];
}

long long f[50][50];
bool caled[50][50];

long long getF(int offset, long long nowE)
{
    if (caled[offset][nowE]) return f[offset][nowE];
    caled[offset][nowE] = true;
    
    long long & ret = f[offset][nowE];
    ret = 0;
    if (offset == N) return ret = 0;
    for (int i = 0; i <= nowE; ++i)
    {
        long long nowGain = i * v[offset];
        long long newE = min(nowE - i + R, E);
        ret = max(ret, nowGain + getF(offset + 1, newE));
    }
    return ret;
}

string deal()
{
    memset(f, 0, sizeof(f));
    memset(caled, false, sizeof(caled));
    long long ans = getF(0, E);
    
    ostringstream ostr;
    ostr << ans;
    return ostr.str();
}

int main()
{
    freopen("/Users/pigoneand/windoflife/CONTEST/CODEJAM/Round1A/b.in", "r", stdin);
    freopen("/Users/pigoneand/windoflife/CONTEST/CODEJAM/Round1A/b.out", "w", stdout);
    
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test)
    {
        init();
        cout << "Case #" << test << ": " << deal() << endl;
    }
    return 0;
}