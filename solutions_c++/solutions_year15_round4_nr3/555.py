#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define getfile sprintf(fin, "%d.in", i); sprintf(fout, "%d.out", i); freopen(fin, "r", stdin); freopen(fout, "w", stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
#include <unordered_map>
#include <unordered_set>
using namespace std;
map<string, int> mp;
char text[22][2022];
vector<int> txt[22];
unordered_set<int> st1, st2;
int main()
{
	fop;
	int T, cas = 0;
	scanf("%d", &T);
	while(T--)
	{
		cerr<<T<<endl;
		mp.clear();
		int n;
		scanf("%d", &n);
		for(int i = 0; i < n; i++)
			txt[i].clear();
		char s1[20101];
		gets(s1);
		gets(s1);
		int len = strlen(s1);
		string ss = "";
		int t = mp.size();
		for(int i = 0; i < len; i++)
		{
			if(s1[i] == ' ')
			{
				t = mp.size();
				if(mp.find(ss) == mp.end())
					mp[ss] = t + 1;
				txt[0].push_back(mp[ss]);
				ss = "";
			}
			else ss += s1[i];
		}
		t = mp.size();
		if(mp.find(ss) == mp.end())
			mp[ss] = t + 1;
		txt[0].push_back(mp[ss]);
		ss = "";
		gets(s1);
		len = strlen(s1);
		for(int i = 0; i < len; i++)
		{
			if(s1[i] == ' ')
			{
				t = mp.size();
				if(mp.find(ss) == mp.end())
					mp[ss] = t + 1;
				txt[1].push_back(mp[ss]);
				ss = "";
			}
			else ss += s1[i];
		}
		t = mp.size();
		if(mp.find(ss) == mp.end())
			mp[ss] = t + 1;
		txt[1].push_back(mp[ss]);
		ss = "";
		for(int i = 2; i < n; i++)
		{
			gets(text[i]);
			ss = "";
			len = strlen(text[i]);
			for(int j = 0; j < len; j++)
			{
				if(text[i][j] == ' ')
				{
					int t = mp.size();
					if(mp.find(ss) == mp.end())
						mp[ss] = t + 1;
					txt[i].push_back(mp[ss]);
					ss = "";
				}
				else ss += text[i][j];
			}
			if(mp.find(ss) == mp.end())
				mp[ss] = t + 1;
			txt[i].push_back(mp[ss]);
		}
		int res = 0x3f3f3f3f;
		for(int i = 0; i < 1 << n - 2; i++)
		{
			st1.clear();
			st2.clear();
			for(int j = 0; j < n; j++)
			{
				if(j == 0)
				{
					int L = txt[j].size();
					for(int k = 0; k < L; k++)
						st1.insert(txt[j][k]);
				}
				else if(j == 1)
				{
					int L = txt[j].size();
					for(int k = 0; k < L; k++)
						st2.insert(txt[j][k]);
				}
				else if(i & (1 << j - 2))
				{
					int L = txt[j].size();
					for(int k = 0; k < L; k++)
						st1.insert(txt[j][k]);
				}
				else
				{
					int L = txt[j].size();
					for(int k = 0; k < L; k++)
						st2.insert(txt[j][k]);
				}
			}
			int nowres = 0;
			int tt = mp.size();
			for(int i = 1; i <= tt; i++)
				if(st1.find(i) != st1.end() && st2.find(i) != st2.end())
					nowres++;
			res = min(res, nowres);
		}
		printf("Case #%d: %d\n", ++cas, res);
	}
}