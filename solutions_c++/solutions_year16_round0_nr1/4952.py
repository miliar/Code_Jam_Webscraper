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


bool visited[15];
int main()
{	
	read("in.txt");
	write("out.txt");
	int t,k,i,s,ta=1;
	long long n,a,b,c;
	sc(t);
	int cnt;
	while(t--)
	{	
		cout<<"Case #"<<ta++<<": ";
		scanf("%lld",&n);
		if(n==0)
		{
			cout<<"INSOMNIA\n";
			continue;
		}
		memset(visited,false,sizeof(visited));
		b=1;cnt=0;
		while(cnt<10)
		{
			a=b*n;
			c=a;
			while(c)
			{
				if(visited[c%10]==false)
				{
					visited[c%10]=true;
					cnt++;
				}
				c=c/10;
			}
			b++;
		}
		cout<<a<<endl;
	}
	return 0;
}
