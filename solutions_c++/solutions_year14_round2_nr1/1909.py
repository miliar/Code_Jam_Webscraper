#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

bool comp(const string &s1,const string &s2)
{
	if(s1.size() !=s2.size()) return s1.size() < s2.size();
	return s1<s2;
}

const int INF=(1<<30);

inline int myget(const string &x,const string &y)
{
	vector<pair<char,int> > v1,v2;
	int i;
	v1.push_back(make_pair(x[0],1));
	for(i=1;i<x.size();i++){
		if(x[i]==v1.back().first) v1[v1.size()-1].second++;
		else v1.push_back(make_pair(x[i],1));
	}
	
	v2.push_back(make_pair(y[0],1));
	for(i=1;i<y.size();i++){
		if(y[i]==v2.back().first) v2[v2.size()-1].second++;
		else v2.push_back(make_pair(y[i],1));
	}

	if(v1.size()!=v2.size()) return -INF;
	int ans=0;
	for(i=0;i<v1.size();i++){
		if(v1[i].first!=v2[i].first) return -INF;
		ans+=abs(v1[i].second - v2[i].second);
	}
	return ans;
}

int main()
{
	int T,tc=1;
	cin >> T;
	for(tc=1;tc<=T;tc++){
		int N,i;
		cin >> N;
		vector<string> v;
		for(i=0;i<N;i++){ string s1; cin >> s1; v.push_back(s1); }
		sort(v.begin(),v.end(),comp);
		int ans=0;
		for(i=1;i<N;i++){
			if(v[i]==v[i-1]) ans=0;
			else ans+=myget(v[i-1],v[i]);
		}
		
		if(ans>-1)
		printf("Case #%d: %d\n",tc,ans);
		else
		printf("Case #%d: Fegla Won\n",tc);
	}
	return 0;
}
