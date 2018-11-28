////////////////////////////////////////////////////////

#include <algorithm>  
#include <iostream>  
#include <sstream>
#include <cstring>
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
using namespace std;  
  
#define MP make_pair   
 
#define FOR(i,a,b) for(int i=(a);i<(b);++i)    
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define SZ(v) ((int)(v).size())
#define REPSZ(i,v) REP(i,SZ(v))
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  

typedef long long LL;  

const int INF = 0x3f3f3f3f;

int T;
string C,J;
string tmpC,tmpJ,ansC,ansJ;
int Len,Ans;

int Sub(string& s1,string& s2)/////////////////
{
	int ret = 0;
	REP(i,Len)ret = 10*ret + s1[i]-s2[i];

	return abs(ret);
}

void dp(int cur)///////////////////////////////
{
	if(cur == Len)
	{
		int ret = Sub(tmpC,tmpJ);
		if(ret < Ans || (ret==Ans&&tmpC<ansC) ||(ret==Ans&&tmpC==ansC&&tmpJ<ansJ))
		{
			Ans = ret;
			ansC = tmpC;
			ansJ = tmpJ;
		}

		return;
	}

	if(C[cur]=='?'&&J[cur]=='?')
	{
		for(int i=0;i<10;i++)
		{
			tmpC += i+'0';
			for(int j=0;j<10;j++)
			{
				tmpJ += j+'0';
				dp(cur+1);
				tmpJ = tmpJ.substr(0,tmpJ.size()-1);
			}
			tmpC = tmpC.substr(0,tmpC.size()-1);
		}
	}
	else if(C[cur]=='?'&&J[cur]!='?')
	{
		tmpJ += J[cur];
		for(int i=0;i<10;i++)
		{
			tmpC += i+'0';
			dp(cur+1);
			tmpC = tmpC.substr(0,tmpC.size()-1);
		}
		tmpJ = tmpJ.substr(0,tmpJ.size()-1);
	}
	else if(C[cur]!='?'&&J[cur]=='?')
	{
		tmpC += C[cur];
		for(int i=0;i<10;i++)
		{
			tmpJ += i+'0';
			dp(cur+1);
			tmpJ = tmpJ.substr(0,tmpJ.size()-1);
		}
		tmpC = tmpC.substr(0,tmpC.size()-1);
	}
	else
	{
		tmpC += C[cur];
		tmpJ += J[cur];
		dp(cur+1);
		tmpC = tmpC.substr(0,tmpC.size()-1);
		tmpJ = tmpJ.substr(0,tmpJ.size()-1);
	}
}

void solve(int kase)/////////////////////////////////
{
	cin >> C >> J;
	Len = C.size();

	Ans = INF;
	tmpC = "";tmpJ = "";

	dp(0);

	printf("Case #%d: ",kase);

	cout << ansC;
	cout << " ";
	cout << ansJ;
	cout << endl;
}

int main()///////////////////////////////////////////
{
//	freopen("..\\input.txt","r",stdin);

	freopen("..\\B-small-attempt1.in","r",stdin);
	freopen("..\\B-small-attempt1.out","w",stdout);

//	freopen("..\\B-large-practice.in","r",stdin);
//	freopen("..\\B-large-practice.out","w",stdout);

	cin >> T;
	REP(i,T)solve(i+1);
	return 0;
}