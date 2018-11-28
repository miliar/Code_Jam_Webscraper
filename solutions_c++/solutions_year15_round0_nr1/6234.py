#include<bits/stdc++.h>
using namespace std;

typedef vector<int> vi; 
typedef pair<int,int> pii;
typedef long long int lld;

#define sz                           size()
#define pb                           push_back 
#define mp                           make_pair
#define F                            first
#define S                            second
#define fill(a,v)                    memset((a),(v),sizeof (a))
#define INF                          INT_MAX
#define mod 1000000007


int main()
{
	int t,n;
	cin>>t;
	for(int T=1;T<=t;T++)
	{
		string xx;
		cin>>n>>xx;
		int a[1010];
		for(int i=0;i<xx.length();i++) a[i] = xx[i]-'0';
		int ans = 0;
		int cnt = 0;
		for(int i=0;i<xx.length();i++)
		{
			if(cnt>=i) cnt+=a[i];
			else 
			{
				ans+=i-cnt;
				cnt+=a[i]+i-cnt;
			}
		}
		cout<<"Case #"<<T<<": "<<ans<<"\n";
	}
	return 0;
}      
