/* */
#include<bits/stdc++.h>

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define UB(X,v) upper_bound(X.begin(), X.end(), v)
#define LB(X,v) lower_bound(X.begin(), X.end(), v)

#define RI(a) scanf("%d", &a)
#define RIL(a) scanf("%lld", &a)
#define PI(a) printf("%d\n", a)
#define PIL(a) printf("%lld\n", a)

#define SZ(a) (int)(a.size())
#define CLR(a) a.clear()

#define SET(a,b) memset(a, b, sizeof(a))
#define LET(a,b) __typeof(a.begin()) b;

#define TR(a,it) for(__typeof(a.begin()) it = a.begin(); it != a.end(); it++)

#define REP(i,l,h) for(int i=(l); i <= (h); i++)
#define DEP(i,h,l) for(int i=(h);i >= (l); i--)

#define ALL(a) a.begin(), a.end()

#define TC()  int tc; cin >> tc;

#define PRSNT(a, e) (a.find(e) != a.end())

#define MINH priority_queue<int, vector<int>, greater<int> >

#define N 100001
#define MOD 1000000007

using namespace std;

#define DBG(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1) {
    cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args) {
    const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}

typedef long long LL;
typedef pair<int, int> PII;
typedef vector< vector<int> > VVI;
typedef vector< pair<int, int> > VPII;
typedef vector<int> VI;

int main()
{
    TC();
    string s;
    int cnt[30], ans[10];
    for(int i=0; i<tc; i++) {
        cin>>s;
        SET(cnt, 0);
        SET(ans, 0);
        REP(j, 0, SZ(s)-1) cnt[s[j]-'A']++;
        ans[0] = cnt['Z'-'A'];
        cnt['Z'-'A'] -= ans[0];
        cnt['E'-'A'] -= ans[0];
        cnt['R'-'A'] -= ans[0];
        cnt['O'-'A'] -= ans[0];
        ans[2] = cnt['W'-'A'];
        cnt['T'-'A'] -= ans[2];
        cnt['W'-'A'] -= ans[2];
        cnt['O'-'A'] -= ans[2];
        ans[4] = cnt['U'-'A'];
        cnt['F'-'A'] -= ans[4];
        cnt['O'-'A'] -= ans[4];
        cnt['U'-'A'] -= ans[4];
        cnt['R'-'A'] -= ans[4];
        ans[6] = cnt['X'-'A'];
        cnt['S'-'A'] -= ans[6];
        cnt['I'-'A'] -= ans[6];
        cnt['X'-'A'] -= ans[6];
        ans[8] = cnt['G'-'A'];
        cnt['E'-'A'] -= ans[8];
        cnt['I'-'A'] -= ans[8];
        cnt['G'-'A'] -= ans[8];
        cnt['H'-'A'] -= ans[8];
        cnt['T'-'A'] -= ans[8];
        ans[3] = cnt['H'-'A'];
        cnt['T'-'A'] -= ans[3];
        cnt['H'-'A'] -= ans[3];
        cnt['R'-'A'] -= ans[3];
        cnt['E'-'A'] -= ans[3];
        cnt['E'-'A'] -= ans[3];
        ans[7] = cnt['S'-'A'];
        cnt['S'-'A'] -= ans[7];
        cnt['E'-'A'] -= ans[7];
        cnt['V'-'A'] -= ans[7];
        cnt['E'-'A'] -= ans[7];
        cnt['N'-'A'] -= ans[7];
        ans[5] = cnt['V'-'A'];
        cnt['F'-'A'] -= ans[5];
        cnt['I'-'A'] -= ans[5];
        cnt['V'-'A'] -= ans[5];
        cnt['E'-'A'] -= ans[5];
        ans[1] = cnt['O'-'A'];
        cnt['O'-'A'] -= ans[1];
        cnt['N'-'A'] -= ans[1];
        cnt['E'-'A'] -= ans[1];
        ans[9] = cnt['I'-'A'];
        cnt['N'-'A'] -= ans[9];
        cnt['I'-'A'] -= ans[9];
        cnt['N'-'A'] -= ans[9];
        cnt['E'-'A'] -= ans[9];
        cout<<"Case #"<<i+1<<": ";
        REP(j, 0, 9) REP(k, 1, ans[j]) cout<<j;
        cout<<endl;
    }
    return 0;
}
