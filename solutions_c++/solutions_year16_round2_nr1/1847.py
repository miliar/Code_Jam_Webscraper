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
		string S;
		cin>> S;
		vector<char> cs(all(S));
		vi cnt(26,0);
		for(int i =0; i < sz(cs);i++)
		{
			int index = cs[i]-'A';
			cnt[index]++;
		}
		string ans = "";
		for(int i =0; i < cnt[25];i++)
			ans+='0';
		for(int i =0; i < max(0,cnt['O'-'A']-cnt[25]-cnt['W'-'A']-cnt['U'-'A']);i++)
			ans+='1';
		for(int i=0; i < cnt['W'-'A'];i++)
			ans+='2';
		for(int i =0; i < max(0,cnt['T'-'A']-cnt['G'-'A']-cnt['W'-'A']);i++)
			ans+='3';
		for(int i=0; i < cnt['U'-'A'];i++)
			ans+='4';
		for(int i =0; i < max(0,cnt['F'-'A']-cnt['U'-'A']);i++)
			ans+='5';
		for(int i=0; i < cnt['X'-'A'];i++)
			ans+='6';
		for(int i =0; i < max(0,cnt['S'-'A']-cnt['X'-'A']);i++)
			ans+='7';
		for(int i=0; i < cnt['G'-'A'];i++)
			ans+='8';
		for(int i =0; i < max(0,cnt['I'-'A']-cnt['X'-'A']-cnt['G'-'A']-cnt['F'-'A']+cnt['U'-'A']);i++)
			ans+='9';

		cout <<"Case #"<<tc<<": "<<ans<<"\n";




	}
}
		



