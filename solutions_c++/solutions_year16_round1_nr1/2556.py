#include<bits/stdc++.h>
using namespace std;

#undef _P
#define _P(...) (void)printf(__VA_ARGS__)
#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",&mark)
#define slld(mark) scanf("%lld",&mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define sz(x) (int((x).size()))
#define PII pair<int,int>
#define PIL pair<int,long long>
#define PLL pair<long long,long long>
#define PIS pair<int,string>
#define MII map<int,int>
#define LL long long
#define FILEIO(name) \
    freopen(name".in", "r", stdin); \
    freopen(name".out", "w", stdout);
#define INF 2000000000 // 2 * 10^9
#define INFLL 1000000000000000000LL  // 10^18
#define mod 1000000007

#define N 512345

string str;
void solve()
{
    cin >> str;
    string cr,s1,s2;
    cr = s1 = s2 = "";
    cr = str[0];
    int l = str.length();
    for(int i=1;i<l;++i)
    {
        s1 = cr+str[i];
        s2 = str[i]+cr;
        cr = max(s1,s2);
    }
    cout << cr << endl;

}

int main()
{
    int t = 1;
    freopen("A-large (1).in","r",stdin);
    freopen("A-large (1).out","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;++i)
    {
        printf("Case #%d: ",i);
        solve();
    }
}


