#include <iostream>
#include <vector>
#include <fstream>
#include <queue>
#include <algorithm>
#include <list>
#include <ctime>
#include <cstdio>
#include <stack>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <functional>
#include <sstream>
#include <map>
#include <set>

#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              1001
#define     MOD               1000000007
#define     Dbug              cout<<"";
#define     EPS               1e-8
#define     timestamp(x)      printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
typedef long long ll;
typedef pair<int, int> pii;
int n;

struct nd
{
	string st;
	int cnt[3];
	nd()
	{
		Rep(i, 3) cnt[i] = 0;
		st = "";
	}
};
int num[500];
nd bt(int r, int p, int s, char ch, int l)
{
	if(l == 0) 
	{
		nd ret;
		ret.st += ch;
		ret.cnt[num[ch]]++;
		return ret;
	}
	nd A, B;
	char op;
	if(ch == 'P') op = 'R';
	else if(ch == 'R') op = 'S';
	else op = 'P';
	A = bt(r, p, s, ch, l-1);
	B = bt(r, p, s, op, l-1);
	if(A.st == "*" || B.st == "*")
	{
		A.st = "*";
		return A;
	}
	if(A.cnt[0] + B.cnt[0] <= p && A.cnt[1] + B.cnt[1] <= r && A.cnt[2] + B.cnt[2] <= s)
	{
		if(A.st > B.st) swap(A, B);
		Rep(i, 3) A.cnt[i] += B.cnt[i];
		A.st += B.st;
		return A;
	}
	else 
	{
		A.st = "*";
		return A;
	}
}
vector<string> ans;
int main() {
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, cas = 1;
	cin>>tc;
	num['P'] = 0, num['R'] = 1, num['S'] = 2;
	while (tc--)
	{
		ans.clear();
		int r, p, s, l;
		cin>>l>>r>>p>>s;
		nd R , P , S;
		if(p) P = bt(r, p , s, 'P', l);
		else P.st = "*";
		if(s) S = bt(r, p, s , 'S', l);
		else S.st = "*";
		if(r) R = bt(r, p, s, 'R', l);
		else R.st = "*";
		if(P.st != "*") ans.push_back(P.st);
		if(S.st != "*") ans.push_back(S.st);
		if(R.st != "*") ans.push_back(R.st);
		if(ans.size() == 0)PF("Case #%d: IMPOSSIBLE\n", cas++);
		else
		{
			Sort(ans);
			PF("Case #%d: ", cas++);
			cout<<ans[0]<<endl;
		}
	}
	return 0;
}