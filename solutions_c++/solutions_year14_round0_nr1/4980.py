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
#include<set>

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
	int t,i,p,a,q,k,j,count,ans;
	set<int> myset;
	sd(t);
	FOR(i,1,t+1)
	{
		myset.clear();
		count=0;
		sd(p);
		FOR(j,1,5)
		{
			FOR(k,0,4)
			{
				cin>>a;
				if(j==p)
				{
					myset.insert(a);	
				}
			}
		}
		sd(q);
		FOR(j,1,5)
		{
			FOR(k,0,4)
			{
				cin>>a;
				if(j==q)
				{
					if(myset.find(a)!=myset.end())
					{
						if(!count)
						{
							ans=a;
						}
						count++;
					}
				}
			}
		}
		cout<<"Case #"<<i<<": ";
		if(count==1)
		{
			cout<<ans<<endl;
		}
		else
		if(count>1)
		{
			cout<<"Bad magician!\n";
		}
		else
		{
			cout<<"Volunteer cheated!\n";
		}
	}
	return 0;
}