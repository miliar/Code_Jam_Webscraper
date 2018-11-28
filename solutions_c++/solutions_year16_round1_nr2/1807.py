/*
name:Hatsune_Miku
*/
#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<map>
#include<queue>
using namespace std;
typedef long long ll;
priority_queue<ll,vector<ll>,greater<ll> > que; 
map<ll,int> m;
map<ll,int>::iterator it;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int k=1;k<=T;k++)
	{
		ll n;
		cin>>n;
		ll num;
		m.clear();
		for (int i=0;i<2*n-1; i+=1)
		{
			for (int j=0;j<n; j+=1)
			{
				scanf("%lld",&num);
				m[num]++;
			}
		}
		printf("Case #%d:",k);
	    for(it=m.begin();it!=m.end();++it){
		int value=it->second;
		if(value%2){
		que.push(it->first);
		}
	}
	while (!que.empty())
	{
		ll ls=que.top();
		que.pop();
		printf(" %lld",ls);
	}
		printf("\n");
	}
	return 0;
}

