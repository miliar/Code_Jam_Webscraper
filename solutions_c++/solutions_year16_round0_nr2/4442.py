#include<bits/stdc++.h>
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++) 
#define F(i,n) for(int i=0;i<n;i++)
#define VE(i,v) for(int i = 0;i < sz(v);i++)
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
		string S;
		cin>> S;
		vector<char> cS(all(S));
		vi bcs(sz(cS),0);
		VE(i,cS)
			if(cS[i]=='+')
				bcs[i]=1;
		int ans = 0;
		int cont = 0;
		VE(i,bcs)
		{
			if(bcs[i]==1)
				cont++;
			else break;
		}
		while(cont != sz(bcs))
		{
			ans++;
			while((bcs[cont]==0) &&( cont <sz(bcs)))
				cont++;
			F(i,cont)
			{
				if(bcs[i]==1) 
					bcs[i]=0;
				else 
					bcs[i]=1;
			}
			cont = 0;
			VE(i,bcs)
			{
				if(bcs[i]==1)
					cont++;
				else break;
			}
		}

		cout <<"Case #"<<tc<<": "<<ans<<"\n";




	}
}
		



