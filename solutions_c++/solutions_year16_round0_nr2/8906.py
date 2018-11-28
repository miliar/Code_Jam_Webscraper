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

int go(string s)
{
	int ans=0;
	int k=0;
	for(int i=s.size()-1;i>=0;i--)
	{
		if(k==0 && s[i]=='-')k=1-k,ans++;else
		if(k==1 && s[i]=='+')k=1-k,ans++;
	}
	
	
	return ans;
}
main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
          cin>>n;
          string x;
          for(i=0;i<n;i++){cin>>x;cout<<"Case #"<<i+1<<": "<<go(x)<<endl;}
          



}
