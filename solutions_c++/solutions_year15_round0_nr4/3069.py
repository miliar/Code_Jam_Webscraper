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
#define __sync__		     std::ios::sync_with_stdio(false);

int main()
{
	__sync__
	int t;
	cin>>t;
	for(int T=1;T<=t;T++)
	{
		int x,r,c;
		bool ok = 0;
		cin>>x>>r>>c;
		if((r*c)%x!=0) ok = 1;
		else
		{
			if(x==3 || x==4 || x==5)
				if(r<x-1 || c<x-1) ok = 1;
			if(x==6)
				if(r<4 || c<4) ok = 1;
			if(x>=7) ok = 1;
		}
		if(ok) cout<<"Case #"<<T<<": RICHARD\n";
		else cout<<"Case #"<<T<<": GABRIEL\n";
	}
	return 0;
}      
