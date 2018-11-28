/*
ID: Tariqul
PROG:
LANG: C++
*/

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define fo(i,j,n) for(i=j;i<n;++i)
#define Fo(i,j,n) for(i=n-1;i>=j;--i)
#define foo(i,j,v) fo(i,j,sz(v))
#define Foo(i,j,v) Fo(i,j,sz(v))
#define li(v) v.begin(),v.end()
#define sz(v) ((int)v.size())
#define CLR(a,v) memset((a),(v),sizeof(a))
#define inf 1000000001
//typedef long long Long;
typedef __int64 Long;
#define pi (2*acos(0))
#define eps 1e-9

#define two(X) (1<<(X))
#define twoL(X) (((Long)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)

char BUFFER[100000 + 5];
bool readn(int &n)	{ return scanf("%d",&n) == 1; }
bool readl(Long &n)	{ return scanf("%I64d",&n) == 1; }
bool readd(double &n){ return scanf("%lf",&n) == 1; }
bool reads(string &s){ s = ""; int n = scanf("%s",BUFFER); if(n == 1)s = BUFFER; return n == 1; }
bool readln(string &s){ char *valid = gets(BUFFER); if(valid)s = BUFFER; return ((bool)valid); }

template<class T>
T gcd(T a,T b) { if(a < b)return gcd(b,a); if(b==0)return a; return gcd(b,a%b); }

set<pair<int,char> > st;
vector<string> ans;
void doit()
{
    int i,n,m,cnt = 0; cin >> n; st.clear(); ans.clear();
    fo(i,0,n)
    {
        cin >> m; st.insert({m,('A' + i)}); cnt += m;
    }
    cnt %= 2;
    set<pair<int,char> >::iterator p1; pair<int,char> pp; string s = "";
    while(sz(st) > 0)
    {
        p1 = st.end(); p1--; pp = *p1; st.erase(p1); s += pp.second; pp.first--; if(pp.first > 0)st.insert(pp);
        if(cnt)
        {
            cnt = 0;
            ans.push_back(s); s = "";
            continue;
        }
        if(sz(st) == 0)break;
        p1 = st.end(); p1--; pp = *p1; st.erase(p1); s += pp.second; pp.first--; if(pp.first > 0)st.insert(pp);
        ans.push_back(s); s = "";
    }
    if(s != "")ans.push_back(s);
    foo(i,0,ans)cout << " " << ans[i];
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Case,t;
	scanf("%d",&t);
	fo(Case,1,t+1)
	{
		printf("Case #%d:",Case);
        doit();
		cout << endl;
	}
	return 0;
}

