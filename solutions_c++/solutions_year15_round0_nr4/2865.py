#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define mod 1000000007

using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector< vector<int> > VVI;
typedef pair< int, int > PII;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int t,Case=0;
	cin>>t;
	while(t--)
	{
		Case++;
		int x,r,c,f; cin>>x>>r>>c; f=0; if(r<c) swap(r,c);
		if((r*c)%x) f=1;
		if(!f)
		{
			if(x==3)
			{
				if(r<2 || c<2) f=1;
			}
			else if(x==4)
			{
				if(r<3 || c<3) f=1;
			}
			else if(x==5)
			{
				if(r<4 || c<4) f=1;
			}
			else if(x==6)
			{
				if(r<4 || c<4) f=1;
			}
			else if(x>=7)
				f=1;
		}
		if(f) cout<<"Case #"<<Case<<": RICHARD\n";
		else cout<<"Case #"<<Case<<": GABRIEL\n";
	}
	return 0;
}
