#include<bits/stdc++.h>
using namespace std;
#define fast cin.sync_with_stdio(0);cin.tie(0)
#define pii pair<int,int>
#define ff first
#define ss second
#define mp make_pair
#define pb push_back
#define INF 99999999
#define N 10001
#define ll long long
#define llu unsigned long long 
#define MOD 1000000007
#define gcd __gcd
#define fill(A,v) memset(A,v,sizeof(A))
int mark[N];
vector<int> ans;
int main()
{
	int t,k,i;
	scanf("%d",&t);
    for(k=1;k<=t;k++)
	{
		int n,i,a,j;
		ans.clear();
		for(i=1;i<N;i++)
		   mark[i]=0;
		scanf("%d",&n);
		for(i=1;i<=2*n-1;i++)
		{
			for(j=1;j<=n;j++)
			{
			  scanf("%d",&a);
			  mark[a]++;
			}  
		}
		for(i=1;i<N;i++)
		{
			if(mark[i]%2==1)
			  ans.pb(i);
		}
		printf("Case #%d: ",k);
		for(i=0;i<ans.size();i++)
		  printf("%d ",ans[i]);
		printf("\n");  
	}
	return 0;
}	