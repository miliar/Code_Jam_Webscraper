#include <cstdio>
#include <algorithm>
#include <vector>
#include<set>
#include<iostream>
#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;
const int MAXN = 15813;
int solve()
{
	int n,x;
	scanf("%d%d",&n,&x);
	int a;
	vector<int> V(n);
	fru(i,n){scanf("%d",&V[i]);}
	int ans=0;
	sort(V.begin(),V.end());
	int iter=n-1;
	fru(i,n)
	{
		while(iter>=0 && V[iter]+V[i]>x)iter--;
		if(iter>i){ans--;iter--;}
		ans++;
	}
	return ans;
}
int main()
{
	int t;
	scanf("%d",&t);
	fru(i,t)printf("Case #%d: %d\n",i+1,solve());
    return 0;
}
