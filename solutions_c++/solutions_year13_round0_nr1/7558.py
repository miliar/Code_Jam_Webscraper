#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <climits>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;
#define sz(x) int((x).size())
#define pb  push_back
#define mp make_pair
#define INI(a,val) memset(a,val,sizeof(a));
#define VI vector<int>
#define VII vector<vector<int> >
#define VS vector<string>
#define VC vector<char>
#define VD vector<double>
#define VF vector<float>
#define SI set<int>
#define SC set<char>
#define SS set<string>
#define MII map<int,int>
#define MSI map<string,int>
#define MIS map<int,string>
#define MIC map<int,char>
#define MCI map<char,int>
#define FOR(i,s,e) for(int (i) = s ; i<=e; i++)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
vector <string>v;
bool completed()
{
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
		if(v[i][j]=='.')
			return 0;
	return 1;
}
bool check(char a)
{
	int i,j;
	bool flag;
	for(i=0;i<4;i++)
	{
		flag=1;
		for(j=0;j<4;j++)
			if(v[i][j]!=a && v[i][j]!='T')
				flag=0;
		if(flag)
			return 1;
	}
	for(i=0;i<4;i++)
	{
		flag=1;
		for(j=0;j<4;j++)
		{
			if(v[j][i]!=a && v[j][i]!='T')
				flag=0;
		}
		if(flag)
			return 1;
	}
	flag=1;
	for(i=0,j=0;i<4 ;i++,j++)
		if(v[i][j]!=a && v[i][j]!='T')
			flag=0;
	if(flag)
	return 1;
	flag=1;
	for(i=3,j=0;i>=0;i--,j++)
		if(v[i][j]!=a && v[i][j]!='T')
			flag=0;
	return flag;
}
int fun()
{
	bool flag1,flag2,draw;
	flag1=flag2=draw=0;
	if(check('O'))
		flag1=1;
	if(check('X'))
		flag2=1;
	if(completed())
		draw=1;
	if(flag1)
		return 0;
	if(flag2)
		return 1;
	if(draw)
		return 2;
	return 3;
}
int main() 
{
	int i,j,t,c=0;
	cin>>t;
	string s;
	while(t--)
	{
		v.clear();
		c++;
		for(i=0;i<4;i++)
		{
			cin>>s;
			v.pb(s);
		}
		int x=fun();
		cout<<"Case #"<<c<<": ";
		if(x==0)
		cout<<"O won\n";
		else if(x==1)
		cout<<"X won\n";
		else if(x==2)
		cout<<"Draw\n";
		else if(x==3)
		cout<<"Game has not completed\n";
		
	}
    	return 0;
}
