#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define rrep(i,x,y) for(i=x;i>=y;i--)
#define trv(y,x) for(typeof(x.begin())y=x.begin();y!=x.end();y++)
#define pb(f) push_back(f)
#define sc(a) scanf("%d",&a)
#define scl(a) scanf("%lld",&a)
#define pi(c) printf("%d\n",c)
#define pil(c) printf("%lld\n",c)
#define ll long long int
#define scs(a) scanf("%s",a)
using namespace std;
#define mod 1000000007
FILE *fin = freopen("1.in","r",stdin);
FILE *fout = freopen("out.txt","w",stdout);
 

#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
 

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< pii > vpii;

int main()
{
	int t;
	int casse=1;
	sc(t);
	while(t--)
	{
		int n;
		cin>>n;
		int a[n+1];
		int i,j,k;
		for(i=1;i<=n;i++)
		{
			cin>>a[i];
		}
		int ans1=0,mini=-999;
		for(i=1;i<=n-1;i++)
		{
			if(a[i]>a[i+1])
			{
				ans1+=a[i]-a[i+1];
				mini=max(mini,a[i]-a[i+1]);
			}
			
		}
	//	cout<<mini<<endl;
		int ans2=0;
		for(i=1;i<=n-1;i++)
		{
		//	if(mini>a[i])
			if(mini!=-999)
			ans2+=min(mini,a[i]);
		}
		cout<<"Case #"<<casse<<": "<<ans1<<" "<<ans2<<endl;
		casse++;
		
		
	}
}

