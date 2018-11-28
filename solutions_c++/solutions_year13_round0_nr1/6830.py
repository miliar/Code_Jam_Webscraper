#include<cstdio>
#include<vector>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<queue>
#include<set>
#include<stack>
#include<map>
#include<sstream>
#include<bitset>
#include<deque>
#include<utility>
#include<cstdlib>
#include<iomanip>
#include<cctype>
#include<climits>
#include<iostream>
using namespace std;
#define ll             long long
#define ull            unsigned long long
#define all(x)         x.begin(),x.end()
#define vi             vector<int>
#define vvi            vector<vector<int> >
#define INF            2147483647
#define LIMIT          1000
#define mod            1000000007
#define pi             pair<int,int>
#define mp             make_pair
#define pb(v)          v.push_back
#define sz(x)          x.size()
string tostr(ll x)     { stringstream ss; ss << x; return ss.str(); }
ll toint(string &s)    { stringstream ss; ss << s; long long x; ss >> x; return x; }
ll gcd(ll a,ll b){return b?gcd(b,a%b):a;}

int main()
{
    #ifndef ONLINE_JUDGE
     freopen("A-large.in","r",stdin);
     freopen("output.txt","w",stdout);
    #endif
	 int t;
	 cin>>t;
	 for(int test=1;test<=t;test++)
	 {
		 char mat[5][5];
		 for(int i=0;i<5;i++)for(int j=0;j<5;j++)mat[i][j]='z';
		 for(int i=1;i<=4;i++)
			 for(int j=1;j<=4;j++)
				 cin>>mat[i][j];
		 int cnt1=0,cnt12=0,cnt13=0,cnt14=0,cnt2=0,cnt22=0,cnt23=0,cnt24=0,cnt3=0;
		 for(int i=1;i<=4;i++)
			 for(int j=1;j<=4;j++)
				 if(mat[i][j]=='X'||mat[i][j]=='T'||mat[i][j]=='O')
					 cnt3++;
		 for(int i=1;i<=4;i++)if(mat[i][i]=='T'||mat[i][i]=='X')cnt1++;
		 for(int i=1;i<=4;i++)if(mat[4-i+1][i]=='T'||mat[4-i+1][i]=='X')cnt14++;
		 for(int i=1;i<=4;i++)
		 {
			 cnt12=0;
			 for(int j=1;j<=4;j++)
				 if(mat[i][j]=='X'||mat[i][j]=='T')cnt12++;
			 if(cnt12==4)break;
		 }
		 for(int i=1;i<=4;i++)
		 {
			 cnt13=0;
			 for(int j=1;j<=4;j++)
				 if(mat[j][i]=='X'||mat[j][i]=='T')cnt13++;
			 if(cnt13==4)break;
		 }
		 int ans=max(max(cnt1,cnt14),max(cnt12,cnt13));
		 if(ans==4){cout<<"Case #"<<test<<": "<<"X won\n";continue;}
		 for(int i=1;i<=4;i++)if(mat[i][i]=='T'||mat[i][i]=='O')cnt2++;
		 for(int i=1;i<=4;i++)if(mat[4-i+1][i]=='T'||mat[4-i+1][i]=='O')cnt24++;
		 for(int i=1;i<=4;i++)
		 {
			 cnt22=0;
			 for(int j=1;j<=4;j++)
				 if(mat[i][j]=='O'||mat[i][j]=='T')cnt22++;
			 if(cnt22==4)break;
		 }
		 for(int i=1;i<=4;i++)
		 {
			 cnt23=0;
			 for(int j=1;j<=4;j++)
				 if(mat[j][i]=='O'||mat[j][i]=='T')cnt23++;
			 if(cnt23==4)break;
		 }
		 ans=max(max(cnt2,cnt24),max(cnt22,cnt23));
		 if(ans==4){cout<<"Case #"<<test<<": "<<"O won\n";continue;}
		 else if(cnt3==16){cout<<"Case #"<<test<<": "<<"Draw\n";continue;}
		 else {cout<<"Case #"<<test<<": "<<"Game has not completed\n";continue;}
	 }
    return 0;
}