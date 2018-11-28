#include<bits/stdc++.h>
using namespace std;
  
#define MOD 1000000007
#define MAX 1000000007
#define gc getchar()  
#define sc(a) scanf("%d",&a)
#define scs(a) scanf("%s",a+1);
#define pri(a) printf("%d\n",a);
#define rep(a,b,c) for(a=b;a<c;a++) 
#define rrep(a,b,c) for(a=b;a>c;a--)  
#define vit vector<int > :: iterator
#define viit vector<ii > :: iterator
#define mp(a,b)  make_pair(a,b)
#define pb(a,b) a.push_back(b)
#define trv(it,v) for(it=v.begin();it!=v.end();it++)
#define F first
#define S second
#define all(v)	v.begin(),v.end()
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define read(a) freopen(a,"r",stdin)
#define write(a) freopen(a,"w",stdout);


int dp[2][500];
int main()
{	
	read("in.txt");
	write("out.txt");
	int i,j,k,n,t,ta=1;
	sc(t);
	string str;
	while(t--)
	{	
		cout<<"Case #"<<ta++<<": ";
		cin>>str;
		n=str.length();
		dp[0][0]=0;dp[1][0]=0;
		for(i=0;i<n;i++)
		{
			if(str[i]=='+')
			{
				dp[0][i+1]=min(dp[0][i],dp[1][i]+2);
				dp[1][i+1]=min(dp[0][i]+1,dp[1][i]+3);
			}
			else if(str[i]=='-')
			{
				dp[0][i+1]=min(dp[1][i]+1,dp[0][i]+3);
				dp[1][i+1]=min(dp[1][i],dp[0][i]+2);
			}
		}
		cout<<dp[0][n]<<endl;
	}
	return 0;
}
