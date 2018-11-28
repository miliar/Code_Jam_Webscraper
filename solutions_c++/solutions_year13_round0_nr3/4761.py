#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <string>
#include <ctime>
#include <cstdlib>
#define Hash1 (LL)11111
#define Hash2 (LL)13337
#define lson l,m,rt << 1
#define rson m + 1,r,rt << 1 | 1
#define eps 1e-8
#define ft first
#define sd second
#define zero(x) (((x)>0?(x):-(x))<eps)
#define LL long long
#define Test puts("END")
#define pi acos(-1.0)
#pragma comment(linker, "/STACK:32000000")
using namespace std;
const int MOD = 1000000007;
const int INF = 1000000000;
const int N = 10000010;
const int M = 1000;

vector<LL> rec;
LL l,r;

void init();
void solve();
inline bool check(LL a);

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    init();
    // for(int i = 0;i < rec.size();i ++)
        // printf("I:%d  rec:%I64d\n",i,rec[i]);
    int cas;
    cin >> cas;
    for(int t = 1;t <= cas;t ++){
        cin >> l >> r;
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}

void init()
{
    for(int i = 1;i < N;i ++){
        if(check(i) && check(i * i))
            rec.push_back(i * i);
    }
}

bool check(LL a)
{
    char s[20];
    itoa(a,s,10);
    int n = strlen(s);
    for(int i = 0;i <= n / 2;i ++){
        if(s[i] != s[n - 1 - i])
            return false;
    }
    return true;
}

void solve()
{
    LL L = lower_bound(rec.begin(), rec.end(),l) - rec.begin();
    LL R = upper_bound(rec.begin(), rec.end(),r) - rec.begin() - 1;
    // printf("L:%I64d   R:%I64d\n",L,R);
    cout << R - L + 1 << endl;
}