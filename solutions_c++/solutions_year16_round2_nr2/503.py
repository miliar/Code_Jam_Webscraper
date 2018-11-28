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
pair<int, pii> path[19][2];
ll dp[19][2], inf = -2, pw[20];
string s, t;

ll rec(int p, int r)
{
	if(p == s.size())
	{
		if(r) return inf;
		return 0;
	}
	if(~dp[p][r]) return dp[p][r];
	ll ans = inf;
	if(s[p]=='?' && t[p]=='?')
	{
		Rep(i, 10)
		{
			Rep(j, 10)
			{
				Rep(rt, 2)
				{
					if(r == 1 && i==0 && j == 9)
						Dbug;

					int c = (r * 10) + i - j - rt;
					if(c < 0 || c > 9) continue;
					ll tmp = rec(p + 1, rt);
					if(tmp != inf)
					{
						tmp = c * pw[s.size() - 1 - p] + tmp;
						if(tmp < ans || ans == inf) 
						{
							ans = tmp;
							path[p][r] = MP(rt, MP(i, j));
						}
					}
				}
			}
		}
	}
	else if(s[p]=='?')
	{
		Rep(i, 10)
		{
			Rep(rt, 2)
			{
				if(i == 8)
					Dbug;
				int c = (r * 10) + i - (t[p] - '0') - rt;
				if(c < 0 || c > 9) continue;
				ll tmp = rec(p + 1, rt);
				if(tmp != inf)
				{
					tmp = c * pw[s.size() - 1 - p] + tmp;
					if(tmp < ans || ans == inf) 
					{
						ans = tmp;
						path[p][r] = MP(rt, MP(i, (t[p] - '0')));
					}
				}
			}
		}
	}
	else if(t[p]=='?')
	{
		Rep(j, 10)
		{
			Rep(rt, 2)
			{
				if(j == 4)
					Dbug;
				int c = (r * 10) + (s[p] - '0') - j - rt;
				if(c < 0 || c > 9) continue;
				ll tmp = rec(p + 1, rt);
				if(tmp != inf)
				{
					tmp = c * pw[s.size() - 1 - p] + tmp;
					if(tmp < ans || ans == inf) 
					{
						ans = tmp;
						path[p][r] = MP(rt, MP((s[p] - '0'), j));
					}
				}
			}
		}
	}
	else
	{
		Rep(rt, 2)
		{
			int c = (r * 10) +  s[p] - t[p] - rt;
			if(c < 0 || c > 9) continue;
			ll tmp = rec(p + 1, rt);
			if(tmp != inf)
			{
				tmp = c * pw[s.size() - 1 - p] + tmp;
				if(tmp < ans || ans == inf) 
				{
					ans = tmp;
					path[p][r] = MP(rt, MP(s[p] - '0' , t[p] - '0'));
				}
			}
		}
	}
	return dp[p][r] = ans;
}
string ansC[2], ansJ[2];
void findPath(int p, int r, bool t)
{
	if(p == s.size()) return;
	int rt = path[p][r].first;
	pii tmp = path[p][r].second;
	ansC[t] += char(tmp.first + '0');
	ansJ[t] += char(tmp.second + '0');
	findPath(p+1, rt, t);
}
int main() {
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc, cas = 1;
	cin>>tc;
	pw[0] = 1;
	For(i, 1, 20) pw[i] = pw[i-1] * 10; 
	while (tc--)
	{
		PF("Case #%d: ", cas++);
		Rep(i, 2) ansC[i].clear(), ansJ[i].clear();
		cin>>s>>t;
		Set(dp, -1);
		ll ans1 = rec(0, 0);
		if(ans1 != inf)
		{
			findPath(0, 0, 0);
		}
		swap(s, t);
		Set(dp, -1);
		ll ans2 = rec(0, 0);
		if(ans2 != inf)
		{
			findPath(0, 0, 2);
			swap(ansC[1], ansJ[1]);
			if(ans1 == inf)
			{
				cout<<ansC[1]<<' '<<ansJ[1]<<endl;
			}
			else
			{
				if(ans1 < ans2 || (ans1==ans2 && (ansC[0]<ansC[1] || (ansC[0]==ansC[1] && ansJ[0]<ansJ[1]))))
				{
					cout<<ansC[0]<<' '<<ansJ[0]<<endl;
				}
				else cout<<ansC[1]<<' '<<ansJ[1]<<endl;
			}
		}
		else
		{
			cout<<ansC[0]<<' '<<ansJ[0]<<endl;
		}
	}
	return 0;
}