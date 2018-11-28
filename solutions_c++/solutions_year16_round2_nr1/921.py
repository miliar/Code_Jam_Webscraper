#include<bits/stdc++.h>
using namespace std;
int arrr[1000005];
#define ll long long int
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define VP vector<pair<int,int> >
#define II pair<int,int> 
#define ll long long int
#define mem(in,rem) memset(in,rem,sizeof(in)) 
#define mp make_pair 
#define sol first
#define Y second
#define pb push_back
#define rep(i,in,b) for(int i=in;i<b;i++)
/*Use like- 
rep(i,0,n - 1)
*/
template<class T> T pwr(T b, T pr){T r=1,sol=b;while(pr){if(pr&1)r*=sol;sol*=sol;pr=(pr>>1);}return r;}
 
#define     inf             (0x7f7f7f7f)
string dp[1005];
long long int inp[3000],n;

int dp1[26],dp2[10];
int main()
{
	freopen("As.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	string s;int T;
	cin>>T;
	for(int t=1;t<=T;++t)
	{
		for(int i=0; i<10;++i)dp2[i]=0;
		for(int i=0; i<26;++i)dp1[i]=0;
		cin >>s;
		for(int i=0; i<s.size();++i)
		{
			dp1[s[i]-'A']++;
			if(s[i]=='W')dp2[2]++;
			if(s[i]=='Z')dp2[0]++;
			if(s[i]=='G')dp2[8]++;
			if(s[i]=='U')dp2[4]++;
			if(s[i]=='X')dp2[6]++;
		}
		dp2[3]=dp1['T'-'A']-dp2[2]-dp2[8];
		dp2[7]=dp1['S'-'A']-dp2[6];
		dp2[5]=dp1['V'-'A']-dp2[7];
		dp2[9]=dp1['I'-'A']-dp2[8]-dp2[6]-dp2[5];
		dp2[1]=dp1['O'-'A']-dp2[2]-dp2[0]-dp2[4];
		cout<<"Case #" <<t<<": ";
		for(int i=0;i<10;++i)
			while(dp2[i]--)
				cout<<i;
		cout<<endl;
	}
	return 0;
}