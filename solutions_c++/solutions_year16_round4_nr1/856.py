#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <list>
#include <cassert>



using namespace std;
#pragma comment(linker, "/STACK:50000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-large(7)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

string dp[14][255];

string go(int deep, char cur)
{
	
	if (deep==0) return string(1,cur);

	if (sz(dp[deep][cur])) return dp[deep][cur];

	string res = "";

	if (cur == 'R')
	{
		res = go(deep-1,'S')+go(deep-1,'R');
		res = min(res, go(deep-1,'R')+go(deep-1,'S'));	
	}

	if (cur == 'S')
	{
		res = go(deep-1,'S')+go(deep-1,'P');
		res = min(res, go(deep-1,'P')+go(deep-1,'S'));	
	}

	if (cur == 'P')
	{
		res = go(deep-1,'P')+go(deep-1,'R');
		res = min(res, go(deep-1,'R')+go(deep-1,'P'));	
	}

	return dp[deep][cur] = res;
}


int a,b,c;
int na,nb,nc;
int check(string s)
{
	a=b=c=0;
	for (int i=0;i<sz(s);i++) {
		if (s[i]=='R') a++;
		if (s[i]=='P') b++;
		if (s[i]=='S') c++;
	}
	return (a==na && b==nb && c==nc);

}

string res = "";

int main()
{
	init();

	int tst;
	scanf("%d\n",&tst);

	for (int cas = 1; cas<=tst; cas++)
	{
	
		res = "";
		int d;
		scanf("%d%d%d%d",&d,&na,&nb,&nc);

		for (int i=0;i<14;i++)
			for (int j=0;j<255;j++)
				dp[i][j] = "";

		string tmp = go(d,'R');
		if (check(tmp)) res = tmp;

		tmp = go(d,'S');
		if (check(tmp)) 
		{
			if (sz(res)==0)
				res = tmp; else
				res = min(res, tmp);
		}

		tmp = go(d,'P');
		if (check(tmp)) 
		{
			if (sz(res)==0)
				res = tmp; else
				res = min(res, tmp);
		}
	
		if (sz(res)==0)
			printf("Case #%d: IMPOSSIBLE\n",cas); else
	
			printf("Case #%d: %s\n",cas,res.c_str());
	}

	


	return 0;
}
