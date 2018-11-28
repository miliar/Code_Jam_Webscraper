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

vector<string> T[4];
int sum(int a)
{
	vector<string> V;
	fru(i,T[a].size())
	{
		int p=T[a][i].size();
		fru(j,p+1)V.push_back(T[a][i].substr(0,j));
	}
	sort(V.begin(),V.end());
	return unique(V.begin(),V.end())-V.begin();
}
int solve()
{
	int n,m;
	scanf("%d%d",&n,&m);
	vector<string> V(n);
	fru(i,n)cin>>V[i];
	int ile=0,wyn=0;
	int ss=1;
	fru(i,n)ss*=m;
	for(int i=0;i<ss;i++)
	{
		fru(j,m)T[j].clear();
		int ii=i;
		fru(p,n)
		{
			T[ii%m].push_back(V[p]);
			ii/=m;
		}
		int k=0;
		fru(j,m)k+=sum(j);
		if(k>wyn){wyn=k;ile=1;}
		else if(wyn==k)ile++;
	}
	printf("%d %d\n",wyn,ile);
	return 0;
	
}
int main()
{
	int t;
	scanf("%d",&t);
	fru(i,t){printf("Case #%d: ",i+1);solve();}
    return 0;
}
