#include <vector>
#include <cassert>
#include <string>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <map>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)

typedef long long ll;

char alpha[]="RPS";

string getbest(int start, int r, int p, int s)
{
	if(r<0 || p<0 || s<0) return "Z";
	if(start==0) r++;
	else if(start==1) p++;
	else s++;
	int n=r+p+s;
	vector<int> res;
	res.push_back(start);
	for(int i=0;(1<<i)<n;i++)
	{
		vector<int> nxt;
		REP(i,res.size())
		{
			nxt.push_back(res[i]);
			nxt.push_back((res[i]+2)%3);
		}
		res=nxt;
	}
	if(r!=count(res.begin(),res.end(),0) || p!=count(res.begin(), res.end(),1) || s!=count(res.begin(), res.end(),2))
		return "Z";
	vector<string> sRes;
	for(int i=0;i<n;i++)
		sRes.push_back(string(1,alpha[res[i]]));
	while(sRes.size()!=1)
	{
		vector<string> nxt;
		for(int i=0;i<sRes.size();i+=2)
		{
			string a=sRes[i];
			string b=sRes[i+1];
			if(a>b) swap(a,b);
			nxt.push_back(a+b);
		}
		sRes=nxt;
	}
	return sRes[0];
}

string solve()
{
	int r,p,s;
	scanf("%*d%d%d%d",&r,&p,&s);
	string res=min(getbest(0,r-1,p,s),min(getbest(1,r,p-1,s), getbest(2,r,p,s-1)));
	if(res[0]=='Z') return "IMPOSSIBLE";
	else return res;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: %s\n",test,solve().c_str());
	}
}
