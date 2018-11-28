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
#include<functional>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pii;
typedef vector<ll> vi;
typedef vi::iterator vit;
typedef set<ll> si;
typedef si::iterator sit;
typedef vector<pii> vpi;
typedef pair<int, char> pci;
typedef vector<pci> vpci;

#define sq(x) ((x)*(x))
#define all(x) (x).begin(),(x).end()
#define cl(x) memset(x,0,sizeof(x))
#define LL "%I64d"
//#define LL "%lld"
#define RLL(x) scanf(LL,&(x))


const int F_SZ = 1111;
int fenw[F_SZ];

void f_add(int pos, int val)
{
    for(; pos < F_SZ; pos += (pos&-pos))
        fenw[pos] += val;
}

int f_get(int pos)
{
    int sum = 0;
    for(; pos > 0; pos -= (pos&-pos))
        sum += fenw[pos];
    return sum;
}

void test(int T)
{
    cl(fenw);
    string s;
    int l;
    cin>>s>>l;
    int answ = 0;
    for(int i = 0; i < s.length(); ++i)
    {
        bool need = (f_get(i+1)&1) ^ (s[i] == '-');
        if(need)
        {
            if(i + l > s.length())
            {
                printf("Case #%d: IMPOSSIBLE\n", T);
                return;
            }
            ++answ;
            f_add(i+1, 1);
            f_add(i+1+l, -1);
        }
    }
    printf("Case #%d: %d\n", T, answ);
    
}

int main()
{
    freopen("/Users/olpet/Downloads/GCJ/a.in", "r", stdin);
    freopen("/Users/olpet/Downloads/GCJ/a.out", "w", stdout);
    int n;
    cin>>n;
    for(int i = 0; i < n; ++i)
        test(i+1);
    return 0;
}
