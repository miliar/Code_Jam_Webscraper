#include<bits/stdc++.h>
using namespace std;
int arrr[1000005];
#define ll long long int
#define VI vector<int>
#define VLL vector<long long int>
#define PQI priority_queue<int>
#define PQLL priority_queue<long long int>
#define VP vector<pair<int,int> >
#define II pair<int,int> 
#define ll long long int
#define mem(in,val) memset(in,val,sizeof(in)) 
#define mp make_pair 
#define sol first
#define Y second
#define pb push_back
#define rep(i,in,b) for(int i=in;i<b;i++)
/*Use like- 
rep(i,0,n - 1)
*/
template<class T> T pwr(T b, T pr){T r=1,sol=b;while(pr){if(pr&1)r*=sol;sol*=sol;pr=(pr>>1);}return r;}
 
#define     inf             (0x7f7f7f7f)
ll pow (ll x,ll y)
{
	if(y<=1)return x;
	
	ll c=pow(x,y/2);
	if(y&1)
	return c*x;
	else return c;
}
int main ()
{
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout); 
	int t,Tcase=1;
	cin>>t;
	while(t--)
	{
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<Tcase<<": ";
		ll u=pow(k,c-1);
		ll z=1;
		for(int i=0;i<s;i++)
		{
			cout<<z<<" ";
			z+=u;
		}
		Tcase++;
		cout<<"\n";
	}
}
