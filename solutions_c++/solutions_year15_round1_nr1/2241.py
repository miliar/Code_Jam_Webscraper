#include <bits/stdc++.h>
#define forall(i,a,b)               for(int i=a;i<=b;i++)
#define pb                          push_back
#define mp			  			    make_pair
#define MOD                         1000000007

#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map <string, int> msi;



int main()
{
	 #ifndef ONLINE_JUDGE
     	freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
     #endif
     ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	forall(kase,1,t)
	{
		int n;
		cin>>n;
		int a[n+1];
		forall(i,0,n-1)cin>>a[i];
		ll ans1=0,ans2=0;
		int mx=-1;
		forall(i,1,n-1)
		{
			if(a[i-1]>a[i])
				ans1+=a[i-1]-a[i];
			mx=max(mx,a[i-1]-a[i]);
		}
		ll left=0;
		forall(i,0,n-2)
		{
			 if(a[i]>=mx)ans2+=mx;
            else ans2+=a[i];
		}

		cout<<"Case #"<<kase<<": "<<ans1<<" "<<ans2<<"\n";
	}
	return 0;
}
