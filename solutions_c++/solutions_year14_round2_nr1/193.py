#include<iostream>
#include<vector>
#include<fstream>
#include<queue>
#include<algorithm>
#include<list>
#include<cstdio>
#include<stack>
#include<cstring>
#include <climits>
#include<cmath>
#include<string>
#include <functional>
#include<sstream>
#include<map>
#include<set>


#pragma comment(linker, "/STACK:100000000000000")

using namespace std;
#define     For(i,a,b)        for (int i=a; i<b; i++)
#define     Rep(i,a)          for (int i=0; i<a; i++)
#define     ALL(v)            (v).begin(),(v).end()
#define     Set(a,x)          memset((a),(x),sizeof(a))
#define     EXIST(a,b)        find(ALL(a),(b))!=(a).end()
#define     Sort(x)           sort(ALL(x))
#define     UNIQUE(v)         Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     MP                make_pair
#define     SF                scanf
#define     PF                printf
#define     MAXN              1001
#define     MAXM              1001
#define     MOD               1000000007
#define     Dbug             cout<<"";
#define     EPS              1e-15
typedef long long ll;
typedef pair<int,int> pii;
int n;
string s[MAXN];
vector<pii> dec(int ind)
{
	vector<pii> v;
	Rep(i, s[ind].size())
	{
		int j=i, cnt=0;
		while(j<s[ind].size() && s[ind][i]==s[ind][j]) j++, cnt++;
		v.push_back(MP(s[ind][i], cnt));
		i=j-1;
	}
	return v;
}
vector<pii> vs[MAXN];
int main(){
	//ios_base::sync_with_stdio(false);
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t, tc=1;
	cin>>t;
	while (t--)
	{
		cin>>n;
		Rep(i, n) cin>>s[i];
		int ans=-1;
		Rep(i, n) vs[i]=dec(i);
		bool can=1;
		Rep(i, n)
		{
			Rep(j, n)
			{
				if(vs[i].size() !=vs[j].size()) 
				{
					can=0;
					break;
				}
				Rep(z, vs[i].size())
				{
					if(vs[i][z].first!=vs[j][z].first) 
					{
						can=0;
						break;
					}
				}
				if(can==0) break;
			}
			if(can==0)
			{
				ans=-1;
				break;
			}
		}
		if(!can) PF("Case #%d: Fegla Won\n", tc++);
		else 
		{
			ans=0;
			Rep(i, vs[0].size())
			{
				int tmp=MOD;
				Rep(j, n)
				{
					int x=0;
					Rep(z, n)
					{
						x+=abs(vs[j][i].second-vs[z][i].second);
					}
					tmp=min(tmp, x);
				}
				ans+=tmp;
			}
			PF("Case #%d: %d\n", tc++, ans);
		}
	}
	
	return 0;
}