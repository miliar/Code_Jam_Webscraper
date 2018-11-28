//Author: Vineet Shah
//IIT Indore
#include<bits/stdc++.h>
#define rep(i,start,lim) for(long long i=start;i<lim;i++)
#define repd(i,start,lim) for(long long i=start;i>=lim;i--)
#define MOD 1000000007
#define scan(x) scanf("%lld",&x)
#define print(x) printf("%lld",x)
#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define br printf("\n")
#define bit(x,i) (x&(1<<i))
using namespace std;
typedef long long lld;
string a[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	lld t;
	cin>>t;
	rep(ttt,1,t+1)
	{
		string x,y="";
		cin>>x;
		lld fr[26]={};
		lld k=x.size();
		rep(i,0,k)
			fr[x[i]-'A']++;
		while(fr['Z'-'A'])
		{
			y+='0';
			rep(i,0,a[0].size())
				fr[a[0][i]-'A']--;
		}
		while(fr['W'-'A'])
		{
			y+='2';
			rep(i,0,a[2].size())
				fr[a[2][i]-'A']--;
		}
		while(fr['U'-'A'])
		{
			y+='4';
			rep(i,0,a[4].size())
				fr[a[4][i]-'A']--;
		}
		while(fr['X'-'A'])
		{
			y+='6';
			rep(i,0,a[6].size())
				fr[a[6][i]-'A']--;
		}
		while(fr['G'-'A'])
		{
			y+='8';
			rep(i,0,a[8].size())
				fr[a[8][i]-'A']--;
		}
		while(fr['O'-'A'])
		{
			y+='1';
			rep(i,0,a[1].size())
				fr[a[1][i]-'A']--;
		}
		while(fr['R'-'A'])
		{
			y+='3';
			rep(i,0,a[3].size())
				fr[a[3][i]-'A']--;
		}
		while(fr['F'-'A'])
		{
			y+='5';
			rep(i,0,a[5].size())
				fr[a[5][i]-'A']--;
		}
		while(fr['I'-'A'])
		{
			y+='9';
			rep(i,0,a[9].size())
				fr[a[9][i]-'A']--;
		}
		while(fr['E'-'A'])
		{
			y+='7';
			rep(i,0,a[7].size())
				fr[a[7][i]-'A']--;
		}
		sort(all(y));
		printf("Case #%lld: ",ttt);
		cout<<y;
		br;
	}
	return 0;
}


