#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long long int lli;
typedef unsigned long long int ulli;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<long> si;
typedef multiset<long> msi;
typedef map<string,long> maps;                               

#define Clear(a) memset(a,0,sizeof a);
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())







int main()
{
	freopen("in2.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int p=1;p<=t;p++)
	{
		int r,c,w;
		scanf("%d %d %d",&r,&c,&w);
		int ans;
		if(c%w==0)ans=(c/w)+w-1;
		else ans=(c/w)+w;
		ans=ans+((c/w)*(r-1));

		printf("Case #%d: %d\n",p,ans);
	}
	return 0;
}


