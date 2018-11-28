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
string st;
bool pal(int k)
{
	int t=k,r=0;
	while(t>0)
	{
		r*=10;
		r+=t%10;
		t/=10;
	}
	if(r==k) return 1;
	return 0;
}
int main(){
	freopen("c.in","r",stdin);
	ofstream cout("c.out");
	int n,tc=1,a,b;
	cin>>n;
	while(n--)
	{
		cin>>a>>b;
		cout<<"Case #"<<tc++<<": ";
		int ans=0;
		for(;a<=b;a++)
		{
			int k=sqrt(a);
			if(k*k==a)
			{
				if(pal(a) && pal(k)) ans++;
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}