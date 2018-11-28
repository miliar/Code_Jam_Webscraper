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
	std::ios::sync_with_stdio(false);
	cin.tie(NULL);
	int T;
	cin >> T;
	for(int tc= 1; tc<= T; tc++)
	{
		string s;
		cin >> s;
		vector<char> sc(all(s));
		char fron = sc[0];
		string ans = "";
		ans = ans + sc[0];
		for(int i =1; i < sz(sc);i++)
		{
			if(sc[i] >= fron)
			{
				ans = sc[i]+ans;
				fron = sc[i];
			}
			else
				ans = ans + sc[i];
		}

		
		cout <<"Case #"<<tc<<": "<<ans<<"\n";




	}
}
		



