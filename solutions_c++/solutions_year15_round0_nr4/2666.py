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
		int n,x,y;
		cin>>n>>x>>y;
		int ans=0;
			if(n==1)
			{
				ans=1;
			}
			else if(n==2)
			{
				if(x&1 && y&1 )
					ans=0;
				else
					ans=1;
			}
			else if(n==3)
			{
				if(x==2&&y==3 || x==3&&y==2 || x==3&&y==4 || x==4&&y==3 || x==3&&y==3)
					ans=1;
				else
					ans=0;
			}
			else if(n==4)
			{
				if(x==4&&y==4 || x==3&&y==4 || x==4&&y==3)
					ans=1;
				else
				 	ans=0;
			}

			string out="";
			if(ans==1)
				out="GABRIEL";
			else
				out="RICHARD";

			cout<<"Case #"<<kase<<": "<<out<<endl;

	}
	return 0;
}
