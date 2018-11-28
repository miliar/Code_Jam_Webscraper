//Copyright © 1993-2014 RishabhJain,Inc
#include <iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<climits>
#include<cmath>
#include<vector>
#include<algorithm>
#include<map>
#include<list>
#include<utility>
 
#define sc(a) scanf("%c",&a)
#define pc(a) printf("%c",a)
#define sd(a) scanf("%d",&a)
#define pd(a) printf("%d\n",a)
#define sll(a) scanf("%lld",&a)
#define pll(a) printf("%lld",a)
#define ss(a) scanf("%s",&a)
#define ps(a) cout<<a
#define FOR(a,b,c) for(a=b;a<c;++a)
#define pii pair<int,int>
#define pub(a) push_back(a)
#define pob() pop_back()
#define puf(a) push_front(a)
#define pof() pop_front()
using namespace std;
int main() {
	// your code goes here
	int t,i,n,j,naomi,count,ken,count2;
	sd(t);
	FOR(i,1,t+1)
	{
		pair<double,int> mypair[1005];
		cin>>n;
		FOR(j,0,n)
		{
			cin>>mypair[j].first;
			mypair[j].second=0;
		}
		FOR(j,n,2*n)
		{
			cin>>mypair[j].first;
			mypair[j].second=1;
		}
		sort(mypair,mypair+2*n);
		naomi=0;
		count=0;
		FOR(j,0,2*n)
		{
			if(mypair[j].second==1)
			{
				if(naomi)
				{
					naomi--;
					count++;
				}
			}
			else
			{
				naomi++;
			}
		}
		ken=0;
		count2=0;
		FOR(j,0,2*n)
		{
			if(mypair[j].second==0)
			{
				if(ken)
				{
					ken--;
					count2++;
				}
			}
			else
			{
				ken++;
			}
		}
		cout<<"Case #"<<i<<": "<<count2<<" "<<n-count<<endl;
	}
	return 0;
}