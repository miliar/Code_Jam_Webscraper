#include<bits/stdc++.h>
#define uniq(c) (c).resize(unique(c.begin(),c.end())-(c).begin());
#define all(a) a.begin(),a.end()
#define FOR(i,a,b) for(long int i=a;i<b;i++)
#define pb push_back
#define PI 3.14159265
#define eps 1e-10
#define LL long long
#define ULL unsigned long long
#define MOD 1000000007



using namespace std;
int SI(string st) {int ans; stringstream s; s<<st; s>>ans; return ans;}
string IS(int n) {string str; stringstream s; s<<n; s>>str; return str;}

int main()
{
	freopen("read.txt","r",stdin);freopen("write.txt","w",stdout);

	int t,r,c,w,tt = 1;
	cin>>t;
	while(t--)
	{
		cin>>r>>c>>w;
		int ans = 0;
		if(w == 1 || w== c)
		ans = c;
		else
		{
			ans = ceil((c*1.0)/w) - 1 + w;
		}
		cout<<"Case #"<<tt<<": "<<ans<<"\n";
		tt++;
	}
	
}
