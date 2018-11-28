#include<bits/stdc++.h>
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


string s1,s2,s3;

int main()
{
	int i,j,k,t,n,m,a,b,c,x,y,z,cs;
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	cin>>t;
	for(cs=1;cs<=t;cs++)
	{
		cin>>s1;
		s2.clear();
		int n1=s1.length();
		for(i=0;i<n1;i++)
		{
			if(i==0)
			{
				s2+=s1[i];
			}
			else
			{
				if(s2[0]>s1[i])
				{
					s2+=s1[i];
				}
				else
				{
					s2.insert(s2.begin(),s1[i]);
				}
			}
		}
		printf("Case #%d: ",cs);
		cout<<s2;
		nl;
	}



	return 0;
}



