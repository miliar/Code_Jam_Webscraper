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
int a[MAX_5],i,m,ans,k,l,j,q,x,n,ma,mi;
string go(string s)
{
	
	string ans="-";
	ans[0]=s[0];
	
	for(int i=1;i<s.size();i++)
	{
		if(ans+s[i]<s[i]+ans)ans=s[i]+ans;else ans+=s[i];
	}
	
	
	
	
	return ans;
}
main()
{

       READ("a.in");WRITE("a.out");
          cin>>n;
          string x;
          for(q=0;q<n;q++){cin>>x;cout<<"Case #"<<q+1<<": "<<go(x)<<endl;}

}
