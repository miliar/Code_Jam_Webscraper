#include<bits/stdc++.h>
#define rep(i,x,y) for(i=x;i<y;i++)
#define rrep(i,x,y) for(i=x;i>=y;i--)
#define trv(y,x) for(typeof(x.begin())y=x.begin();y!=x.end();y++)
#define trvr(y,x) for(typeof(x.rbegin())y=x.rbegin();y!=x.rend();y++)
#define pb(f) push_back(f)
#define pi_ printf("\n")
#define pi(a) printf("%d\n",a)
#define pil(a) printf("%lld\n",a)
#define sc(a) scanf("%d",&a)
#define ll long long
#define scl(a) scanf("%lld",&a)
#define scs(a) scanf("%s",a)
#define mp make_pair
#define fi first
#define se second
#define mod 1000000007
#define inf 1000000009
#define maxn 100009
using namespace std;

//#include<windows.h>
//FILE *fin = freopen("1.in","r",stdin);
FILE *fout = freopen("out.txt","w",stdout);
using namespace std;
typedef pair<int,int> pii;
typedef vector<int > vi;
typedef vector< pii > vpii;
vector<int> primes;
void calculate_prime(int n)
{
	int i,x=n;
	bool a[x+1];
	for(i=2;i<x+1;i++)
	a[i]=true;
	for(i=2;i<sqrt(x)+1;i++)
	{
		if(a[i]==true)
		{
			for(int j=i*i;j<x+1;j+=i)
			{
				a[j]=false;
			}
		}
	}
	for(i=2;i<x+1;i++)
	{
		if(a[i])
		primes.push_back(i);
	}
}
ll P[13][18];
vi ans;
int main()
{
	printf("Case #1: \n");
	calculate_prime(10000);
	int count=0;
//	cout<<primes.size()<<" ";
	int i,j,k,y;
	rep(i,2,11)
	P[i][0]=1;
	rep(i,2,11)
	rep(j,1,17)
	P[i][j]=P[i][j-1]*i;
	int p=1<<15;
	for(i=1<<14;i<p;i++)
	{
	//	cout<<i<<endl;
		y=i;
		ans.clear();
		for(j=2;j<=10;j++)
		{
			ll chk=0;y=i;
			chk+=1;
			for(k=1;k<=15;k++)
			{
				int x=y&1;y>>=1;
				if(x)
				{
					chk+=P[j][k];
				}
			}
	//		cout<<chk<<endl;
			for(k=0;k<primes.size();k++)
			{
				if(chk%primes[k]==0)
				{
					ans.pb(primes[k]);
					break;
				}
			}
			if(ans.size()<j-1) break;
		}
		if(ans.size()==9)
		{
			count++;
			if(count==51) break;
			y=i;
			vi pp;
			pp.pb(1);
			while(y>0) {
				pp.pb(y&1);y>>=1;
			}
			for(k=pp.size()-1;k>=0;k--)
			printf("%d",pp[k]);
			for(j=0;j<9;j++)
			printf(" %d",ans[j]);
			printf("\n");
		}
			
	}
	//cout<<count<<endl;
}
