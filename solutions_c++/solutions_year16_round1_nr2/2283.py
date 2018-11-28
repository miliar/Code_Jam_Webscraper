#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define N 1000001
#define hg ios_base::sync_with_stdio(0);cin.tie(0)
#define ff first
#define ss second
#define gcd __gcd
#define inf (1<<30)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pll pair<ll,ll>
#define bitcit __builtin_popcount
#define mset(x,y) memset(x,y,size(x))
#define INF 1e18
#define ll long long
#define endl "\n"
set<int> s;
set<int>::iterator it;
int fr[2505];
int main() {
    //hg;
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {   s.clear();
        memset(fr,0,sizeof(fr));
    	int n,i;
    	int p,j;
    	scanf("%d",&n);
    	for(i=0;i<2*n-1;i++)
    	{
         for(j=0;j<n;j++)
         {
         	scanf("%d",&p);
         	fr[p]++;
         }
    	}
    	for(i=1;i<2505;i++)
    	{
    		if(fr[i]!=0&&fr[i]%2!=0)
    		s.insert(i);
    	}
    	printf("Case #%d: ",k);
    	for(it=s.begin();it!=s.end();it++)
    	cout<<*it<<" ";
    	cout<<"\n";
    }
	return 0;
}
