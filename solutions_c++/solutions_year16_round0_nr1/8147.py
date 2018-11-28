 # /*Simplicity and Fortitude */
#include <bits/stdc++.h>
#define ff first
#define re return
#define ss second
#define pb push_back
#define mpk make_pair
#define MAXN 1000001
#define MOD 1000000007
#define couts(a) cout<<a<<endl
#define fr(i,a,b) for(ll i=a;i<b;++i)
#define rf(i,a,b) for(ll  i=a;i>=b;--i)
#define coutd(a,b) cout<<a<<" "<<b<<endl
#define ioS ios_base::sync_with_stdio(0);cin.tie(0);
#define coutt(a,b,c)cout<<a<<" "<<b<<" "<<c<<endl;
#define coutar(a,n)  fr(i,0,n)cout<<a[i]<<" ";cout<<endl;
#define coutq(a,b,c,d)cout<<a<<" "<<b<<" "<<c<<" "<<d<<endl;

# define PI 3.141592653589793238462643383279502

using namespace std;
typedef long long int ll;
typedef long double ld;
typedef pair<int,int>pi;
typedef long long int ll;
typedef vector<int> vi;

ll a[13],ct=0;

void fd(ll x)
{
	ll t=x;
	while(t!=0)
	{
		int y=t%10;
		if(a[y]==0){ct++;a[y]++;}

		if(ct==10){re ;}

		t/=10;
	}

}


int main()
{

freopen("input2.in","r",stdin);
freopen("output.txt","w",stdout);
ll t;
cin>>t;
fr(i,1,t+1){
ll n;
cin>>n;
if(n==0){cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl; continue;}
ll y=1;
while(ct<10){fd(y*n);y++; }

cout<<"Case #"<<i<<": "<<(y-1)*n<<endl;

fr(i,0,10)a[i]=0;
ct=0;
}
}
