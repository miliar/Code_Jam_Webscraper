#include <iostream>
#include <stdio.h>
#include <sstream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <unordered_set>
#include <cmath>
#include <queue>
#include <ctime>
#include <functional>

using namespace std;

#pragma comment(linker, "/STACK:2000000")

#define CLR(a,x) memset(a,x,sizeof a)
#define LL long long
#define ALL(v) v.begin(),v.end()
#define FR(i,n) for(LL i=0;i<(LL)n;i++)
#define FAB(i,a,b) for(LL i=(LL)a;i<(LL)b;i++)
#define FBA(i,b,a) for(LL i=(LL)b;i>=(LL)a;i--)
#define IIN(x) scanf("%d",&x)
#define IIN2(x,y) scanf_s("%d%d",&x,&y)
#define LIN(x) scanf_s("%I64d",&x)
#define LIN2(x,y) scanf_s("%I64d%I64d",&x,&y)
#define EXIT(n) {cout<<n<<endl;return 0;}
#define PII pair<LL,int>
#define PPI pair<PII,int>
#define PPP pair<PII,PII>
#define PLL pair<LL,LL>
#define PPL pair<LL,PLL>
#define PDD pair<double,double>
#define PDI pair<double,int>
#define PIS pair<int,string>
#define PSI pair<string,int>
#define BIT(mask,i) ((mask>>i)&1)
#define PI 3.141592653589793238
#define VI vector<int>
#define VPI vector<PII>
#define VLL vector<LL>
#define VPL vector<PLL>
#define VS vector<string>
#define VVI vector<VI>
#define SI set<int>
#define SLL set<LL>
#define SLP set<PPL>
#define SPI set<PII>
#define SS set<string>
#define MII map<int,int>
#define MLL map<LL,LL>
#define MIP map<int,PII>
#define MSI map<string,int>
#define MSL map<string,LL>
#define MIS map<int,string>
#define INF 2000000000000000000
#define MOD (1000*1000*1000+9)
#define MAX (100*1000+10)

int t, q;
int n, cnt, res;
string s;

void input()
{
	cin >> n >> s;
}

void solve()
{
	cnt = res = 0;
	FR(i, s.size())
	{
		int t = 0;
		if (i - cnt > 0) t = i - cnt;
		res += t;
		cnt += (s[i] - '0' + t);
	}
}

void output()
{
	cout << "Case #" << q << ": " << res << endl;
}


int main()
{
	//FILE *stream; freopen_s(&stream, "in.txt", "r", stdin);
	//freopen_s(&stream, "out.txt", "w", stdout);

	
	cin >> t;
	for (q = 1; q <= t; q++)
	{
		input();
		solve();
		output();
	}
	
	return 0;
}