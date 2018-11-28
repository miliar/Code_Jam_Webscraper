#include <vector>
#include <string>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
typedef int ll;
#define REP(i,n) for(int i=0;i<(n);i++)

int lcp(const string& a, const string& b)
{
	if(a.empty()||b.empty()) return -1;
	int res=0;
	for(int i=0;i<a.size() && i<b.size();i++)
	{
		if(a[i]!=b[i]) break;
		res=i+1;
	}
	return res;
}

pair<int,int> update(pair<int,int> a, pair<int,int> b)
{
	if(a.first==b.first)
		return make_pair(a.first,a.second+b.second);
	else return max(a,b);
}

pair<int,int> solve(int cur, vector<string>& v, int n, string &A, string &B, string &C, string &D, int cur_cnt)
{
	if(cur==v.size())
		return make_pair(cur_cnt,1);
	pair<int,int> res(0,0);
	for(int i=0;i<n;i++)
	{
		if(i==0)
		{
			res=update(res,solve(cur+1,v,n,v[cur],B,C,D,cur_cnt+v[cur].length()-lcp(A,v[cur])));
		}
		else if(i==1)
		{
			res=update(res,solve(cur+1,v,n,A,v[cur],C,D,cur_cnt+v[cur].length()-lcp(B,v[cur])));
		}
		else if(i==2)
		{
			res=update(res,solve(cur+1,v,n,A,B,v[cur],D,cur_cnt+v[cur].length()-lcp(C,v[cur])));
		}
		else if(i==3)
		{
			res=update(res,solve(cur+1,v,n,A,B,C,v[cur],cur_cnt+v[cur].length()-lcp(D,v[cur])));
		}
	}
	return res;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		int m,n;
		scanf("%d%d",&m,&n);
		vector<string> v;
		REP(i,m)
		{
			string s;
			cin>>s;
			v.push_back(s);
		}
		sort(v.begin(),v.end());
		string empty = "";
		pair<int, int> res = solve(0, v, n, empty, empty, empty, empty,0);
		printf("Case #%d: %d %d\n",test,res.first, res.second);
	}
	return 0;
}
