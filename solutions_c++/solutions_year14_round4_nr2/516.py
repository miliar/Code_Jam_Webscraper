#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<set>
#include<vector>
#include<map>
#include<deque>
#include<cstdlib>
#include<functional>
#include<utility>
#include<ctime>
#include<sstream>
#define pb push_back
#define mp make_pair
#define fr(i,n) for(int i=0;i<n;++i)
#define fn(i,n) for(int i=n-1;i>=0;--i)
#define fe(i,a) for(__typeof(a.begin()) i=a.begin();i!=a.end();++i)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;
const int N = 1010;
vector<int> a;
int ans,pos,test,n,x;


int main()
{
	scanf("%d",&test);
	for (int t=1;t<=test;++t)
	{
		scanf("%d",&n);
		for (int i=0;i<n;i++)
		{
			scanf("%d",&x);
			a.pb(x);
		}
		ans=0;
		for (int i=0;i<n;i++)
		{
			int pos=0;
			vector<int>::iterator it=a.begin(),it2 = it;
			for (int j=0;j<a.size();j++,it++)
				if (a[j]<a[pos])
					pos=j, it2=it;
			ans+=min(pos,(int)a.size()-pos-1);
			a.erase(it2);
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
