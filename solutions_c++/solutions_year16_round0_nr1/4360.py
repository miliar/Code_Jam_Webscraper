#include<bits/stdc++.h>
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++) 
#define F(i,n) for(int i=0;i<n;i++)
#define VE(i,v) for(int i = 0;i < (v).size();i++)
using namespace std;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned int ui;
const double PI  =3.141592;

int main()
{
	//std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	for(int tc= 1; tc<= T; tc++)
	{
		ll N;
		cin>> N;
		set<int> dig;
		ll ans= 0;
		if(N==0)
		{
			cout <<"Case #"<<tc<<": INSOMNIA\n";
			continue;
		}
		while(sz(dig)!=10)
		{
			ll temp = ans;
			while(temp!=0)
			{
				int d = temp%10;
				dig.insert(d);
				temp = temp/10;
			}
			if(sz(dig)!=10)
				ans+=N;
		}
		cout <<"Case #"<<tc<<": "<<ans<<"\n";




	}
}
		



