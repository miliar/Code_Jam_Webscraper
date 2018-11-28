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


int main()
{	
	read("input.in");
	write("output.out");
	int i,j,k,n,ta=0,t;
	sc(t);
	while(t--)
	{
		ta++;
		printf("Case #%d: ",ta);
		string ans,a,b,inp;
		cin>>inp;
		for(i=0;i<inp.size();i++)
		{
			if(inp[i]+ans>ans+inp[i])
			ans=inp[i]+ans;
			else
			ans=ans+inp[i];
		}
		cout<<ans<<endl;
	}

	return 0;
}
