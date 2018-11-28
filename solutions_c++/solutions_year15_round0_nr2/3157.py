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
#define pans1ent(c,x) ((c).find(x) != (c).end()) 
#define cpans1ent(c,x) (find(all(c),x) != (c).end())





int A[1003];

int main()
{
	Clear(A);
	freopen("in1.in","r",stdin);
	freopen("out.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<=n;i++)
		{
			scanf("%d",&A[i]);
		}
		ll ans=10000000;
		ll ans1;
		ll ans2=0;
		for(int i=1;i<=1000;i++)
		{
			ans1=i;
			for(int j=0;j<n;j++)
			{
				if(A[j]>i)
				{
					int div =(A[j]/i);
					if(A[j]%i==0)
					{
						ans1=ans1+div-1;
					}
					else ans1=ans1+div;
				}
				else ans2++;
			}
			ans=min(ans,ans1);
		}
		printf("Case #%d: %lld\n",c,ans);
	}
	return 0;
}


