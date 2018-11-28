#include<iostream>
#include<vector>
#include<fstream>
#include<queue>
#include<algorithm>
#include<list>
#include<cstdio>
#include<stack>
#include<cstring>
#include<cmath>
#include<string>
#include<map>
using namespace std;
#define     FOR(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     FIT(it,v)         for (typeof((v).begin())it=(v).begin(); it!=(v).end(); ++it)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     GSORT(x)          sort(ALL(x), greater<typeof(*((x).begin()))>())
#define     UNIQUE(v)         SORT(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
typedef long long ll;
typedef pair<int,int> pii;
int n;
string st;
int main(){
	freopen("b.in","r",stdin);
	ofstream cout("b.out");
	int tc=1, t, m, a[101][101];
	cin>>t;
	while(t--)
	{
		cin>>n>>m;
		cout<<"Case #"<<tc++<<": ";
		Rep(i,n) Rep(j,m) cin>>a[i][j];
		bool sw=0;
		Rep(i,n)
		{
			Rep(j,m)
			{
				sw=0;
				int l=0, u=0;
				Rep(k,m) if(a[i][j]!=a[i][k]) l=max(l,a[i][k]);
				if(l>a[i][j])  
					sw=1;
				else continue;
				Rep(k,n) if(a[i][j]!=a[k][j]) u=max(u,a[k][j]);
				if(u>a[i][j]) 
				{
					if(sw==1)
					{
						i=n;
						cout<<"NO\n";
						break;
					}
					sw=0;
				}
				else sw=0;
			}
		}
		if(!sw) cout<<"YES\n";
	}
	return 0;
}