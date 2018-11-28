#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long 
#define ll long long
#define MAX 100
#define pb push_back
#define gc getchar
#define mp make_pair
#define fast(){cin.sync_with_stdio(0);cin.tie(0);cout.tie(0);}
bool fun(ll n, vector<bool>&a)
{
	ll m=n;
	while(m>0)
	{
		a[m%10]=1;
		m/=10;
	}
	for(int i=0;i<10;i++)
		if(!a[i])
		 return true;
	
	return false;
	
}
int main()
{
	int t;
	//freopen("A-large.in","r+",stdin);
	//freopen("output1.txt","w+",stdout);
	cin>>t;
	int cases=0;
	while(t--)
	{
		cases++;
		ll n;
		cin>>n;
		ll temp=n;
		ll i=1;
		ll prev=n;
		bool flag=0;
		vector<bool>a(10,0);
		while(fun(n,a))
		{
			n=(i+1)*temp;
			if(n==prev){
				flag=1;
				break;
			}
			prev=n;
			i++;
		}
		cout<<"Case #"<<cases<<": ";
		if(flag)
			cout<<"INSOMNIA\n";
		else
			cout<<n<<"\n";
	}
}
