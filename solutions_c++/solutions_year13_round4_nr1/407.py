#include <algorithm>
#include <numeric>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <stack>
using namespace std;

const int MOD=1000002013;
long long mas[2005];

bool vh(pair<int,int> p1, pair<int,int> p2)
{
	if (p1.first>p2.first)
		swap(p1,p2);
	return (p1.second>p2.second || p1.second<p2.first);
}

void solveCase(int t)
{
	int res=0;
	int N,M;
	cin>>N>>M;
	vector<pair<pair<int,int>,int> > v,v1;
	long long total1=0,total2=0;
	set<int> s;
	map<int,int> a;
	vector<int> vv;
	memset(mas,0,sizeof(mas));
	for (int i=0;i<M;i++)
	{
		pair<pair<int,int>,int> ps;
		cin>>ps.first.first>>ps.first.second>>ps.second;
		s.insert(ps.first.first);
		s.insert(ps.first.second);
		v.push_back(ps);
		long long cur=ps.first.second-ps.first.first;
		cur*=(N+N-cur+1);
		cur/=2;
		cur%=MOD;
		cur*=ps.second;
		cur%=MOD;
		total1+=cur;
	}
	total1%=MOD;
	int cnt=1;
	for (auto i=s.begin();i!=s.end();i++)
	{
		a[*i]=cnt++;
		vv.push_back(*i);
	}
	for (int i=0;i<M;i++)
	{
		int l=a[v[i].first.first];
		int r=a[v[i].first.second];
		for (int j=l;j<r;j++)
			mas[j]+=v[i].second;
	}
	int cur=0;
	while (true)
	{
		while(cur<2005 && mas[cur]==0)
			cur++;
		if (cur>2004)
			break;
		int cur1=cur;
		long long minp=mas[cur];
		while (cur1<2005 && mas[cur1]!=0)
		{
			minp=min(minp,mas[cur1]);
			cur1++;			
		}
		long long res=vv[cur1-1]-vv[cur-1];
		res*=(2*N-res+1);
		res/=2;
		res%=MOD;
		res*=minp;
		res%=MOD;
		total2+=res;
		for (int i=cur;i<cur1;i++)
			mas[i]-=minp;
	}
	total2%=MOD;
	int ret=(total1+MOD-total2)%MOD;
	printf("Case #%d: %d\n",t,ret);
}

int main()
{
   freopen("in.in", "rt", stdin);
   freopen("out.out", "wt", stdout);
   int n;
   cin>>n;
   for (int i=0;i<n;i++)
	   solveCase(i+1);
   return 0;
}