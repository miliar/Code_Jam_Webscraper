using namespace std;
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<bitset>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<sstream>
#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define rep(i,n) for(i=1;i<=n;++i)
#define max(a,b) ((a)>(b))?(a):(b)
typedef  long long int ull;



int fn(string s)
{
	
	int i,l=s.length(),con=0,ans=0;
	
	for(i=0;i<l;i++)
	{
		if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' )con=0;
		else con++;
		ans=max(ans,con);
	}
	return ans;
}

int main()
{
	
	int t,n,i,j,ans,tt=1,l;
	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
	read(t);
	string s;
	while(t--)
	{
		cin>>s;
		cin>>n;
		ans=0;
		l=s.length();
		for(i=0;i<l;i++)
		for(j=1;j<=l-i;j++)
		{
			
			string ss=s.substr(i,j);
			//cout<<ss<<endl;
			if(fn(ss)>=n)ans++;
		}
		printf("Case #%d: %d\n",tt++,ans);
		
	}
//
}

