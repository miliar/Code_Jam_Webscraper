#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<queue>
#include<vector>
#include<set>
#include<stack>
#include<map>
#include<utility>

#define ll long long int
#define F first
#define S second
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define rep(i,in1,n) for(i=in1;i<=n;i++)
#define repd(i,in1,n) for(i=in1;i>=n;i--)

#define pf(n) printf("%d ",n);
#define sf(n) scanf("%d",&n)
#define sl(n) scanf("%I64d",&n)
#define nl printf("\n")
#define mem(arr,init) memset(arr,init,sizeof(arr))
#define vi vector<int>
#define vvi vector<vi>

#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define mp make_pair
#define ep emplace_back//c++11
#define ii pair<int,int>
#define iii pair<ii,i>
//	freopen("input.txt","r",stdin);
  //  freopen("output.txt","w",stdout);
using namespace std;
string s1;
int main()
{
	int i,j,k,t,n,m,a,b,c,x,y,z,cs;
	freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
	cin>>t;
	int ans;
	cs=1;
	while(t--)
	{
		cin>>s1;
		n=s1.length();
		int ptr=-1;
		ans=0;
		for(i=0;i<n;i++)
		{
			if(s1[i]=='-')
			{
				ptr=i;
			}
		}
		int ptr2=-1;
		while(ptr>=0)
		{
			ptr2=-1;
			ans++;
			for(i=0;i<=ptr;i++)
			{
				
				if(s1[i]=='+')
				{
					s1[i]='-';
					ptr2=i;
				}
				else
					s1[i]='+';
			}
			ptr=ptr2;

		}
		printf("Case #%d: ",cs++);
		cout<<ans;
		nl;

	}


	return 0;
}