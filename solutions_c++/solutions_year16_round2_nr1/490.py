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
#define     MAXN              3001
#define     MOD               1000000007
#define     Dbug              cout<<"";
#define     EPS               1e-8
#define     timestamp(x)      printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
typedef long long ll;
typedef pair<int, int> pii;
int n, cnt[30], ans[10];
string st;
void calc(string s, int c, int num)
{
	ans[num] += c;
	Rep(i, s.size()) cnt[s[i]-'A'] -= c;
}
int main() {
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, cas = 1;
	cin>>tc;
	while(tc--)
	{
		Set(cnt, 0);
		Set(ans, 0);
		cin>>st;
		Rep(i, st.size())
		{
			cnt[st[i] - 'A'] ++;
		}
		PF("Case #%d: ", cas++);
		calc("ZERO", cnt['Z' - 'A'], 0);
		calc("TWO", cnt['W' - 'A'], 2);
		calc("FOUR", cnt['U' - 'A'], 4);
		calc("SIX", cnt['X' - 'A'], 6);
		calc("EIGHT", cnt['G' - 'A'], 8);
		calc("ONE", cnt['O' - 'A'], 1);
		calc("THREE", cnt['H' - 'A'], 3);
		calc("FIVE", cnt['F' - 'A'], 5);
		calc("SEVEN", cnt['V' - 'A'], 7);
		calc("NINE", cnt['E' - 'A'], 9);
		Rep(i, 10) Rep(j, ans[i]) cout<<i;
		cout<<endl;
	}
	return 0;
}