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
		int smax;
		cin>>smax;
		string s;
		cin>>s;
		ll standing=s[0]-'0';
		ll ans=0;
		forall(i,1,s.length()-1)
		{
			int k=s[i]-'0';
			int ans2=0;
			if(k!=0)
				if(i>standing)ans2+=i-standing;
			standing+=k+ans2;

			ans+=ans2;
		}
		cout<<"Case #"<<kase<<": "<<ans<<endl;

	}
	return 0;
}
