// __   _   _   _   _____   _   _   _____   _   _       ___
//|  \ | | | | | | /  ___| | | | | /  ___/ | | | |     /   |
//|   \| | | | | | | |     | | | | | |___  | |_| |    / /| |
//| |\   | | | | | | |  _  | | | | \___  \ |  _  |   / / | |
//| | \  | | |_| | | |_| | | |_| |  ___| | | | | |  / /  | |
//|_|  \_| \_____/ \_____/ \_____/ /_____/ |_| |_| /_/   |_|

#include<bits/stdc++.h>
#define PB(x) push_back(x)
#define MP(x, y) make_pair(x, y)
#define fi first
#define se second
#define ll long long
#define pii pair< int, int >
#define MEM(p, v) memset(p, v, sizeof(p))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)
#define S system("pause")
#define R return(0)
#define INF int(1e9)
#define MAX_5 int(1e5+5)
#define MAX_6 int(1e6+6)
#define ll long long
#define tree int h,int l1,int r1
#define left 2*h,l1,(l1+r1)/2
#define right 2*h+1,(l1+r1)/2+1,r1
using namespace std;
int a[MAX_5],b[MAX_5],f[MAX_5],i,m,ans,k,l,j,q,x,n,ma,mi;
string s;

string go(int x)
{
	
	for(int i=0;i<10;i++)f[i]=0;
	
	
	for(int i=1;i<=100000000;i++)
	{
		ll y=1LL*x*i;
		
		while(y)
		{
			f[y%10]=1;
			y/=10;
		}
		int F=1;
		for(int i=0;i<10;i++)if(!f[i])F=0;
		
		if(F)
		{
			y=1LL*x*i;
			
				string s;
				
			while(y)
			{
				s=char(y%10+'0')+s;
				y/=10;
			}
			
			return s;
		}
		
	}
	
	
	
	
	return "INSOMNIA";
}
main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
          cin>>n;
          int x;
          for(i=0;i<n;i++){cin>>x;cout<<"Case #"<<i+1<<": "<<go(x)<<endl;}
          



}
