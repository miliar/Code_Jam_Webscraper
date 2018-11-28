#include<bits/stdc++.h>
using namespace std;
#define no 31623
//#define getchar_unlocked getchar
#define ll long long int
#define mb make_pair
#define pb push_back
#define F first
#define S second
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define tr(it,x) for(auto it=x.begin(); it!=x.end(); it++)
#define rep(i,n) for(int i=0;i<n;i++)
#define repp(i,a,b) for(int i=a;i<=b;i++)
#define ref(i,n) for(int i=n;i>1;i--)
#define reff(i,a,b) for(int i=a;i>=b;i--)
#define M 1000000007
#define MAX 100005 
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
//#define sc(x) scanf("%d",&x)
//#define scc(x1,x2) scanf("%d%d",&x1,&x2)
//#define sccc(x1,x2,x3) scanf("%d%d%d",&x1,&x2,&x3)
//#define scl(x) scanf("%lld",&x)
//#define sccl(x1,x2) scanf("%lld%lld",&x1,&x2)
//#define sccl(x1,x2,x3,x4,x5) scanf("%lld%lld%lld%lld%lld",&x1,&x2,&x3,&x4,&x5)
//#define pr(x) printf("%f\n",x)
//#define prl(x) printf("%lld\n",x)
//#define prrl(x1,x2) printf("%lld %lld\n",x1,x2)
#define fill(a,x) memset(a,x,sizeof(a))
ll gcd(ll a, ll b) { return (b == 0 ? a : gcd(b, a % b)); }
ll lcm(int a, int b) { return (a * (b / gcd(a, b))); }
ll max(ll a,ll b,ll c){return max(a,max(b,c));}
ll power(ll x,ll y)
{
    ll ans=1;
    while(y>0){
        if(y&1)
            ans=(ans*x)%M;
        x=(x*x)%M;
        y/=2;
    }
    return ans;
}
ifstream ifs("Subtask1.txt");
ofstream ofs("Solution1.txt");
int main()
{
	ll t,n,cnti=1,m;
	//cin>>t;
	ifs>>t;
	while(t--)
	{
		//ifs>>n;
	     string s;
	     ifs>>s;
	     ll a[26];
	     fill(a,0);
		 m=s.size();
		 //cout<<s;
		 rep(i,m)
	    { 
	      a[s[i]-'A']++;	 
		}
		ll k=0;
		char c[2000];
		//cout<<a[25]<<" "<<a[4]<<" "<<a[14]<<endl;
		ofs<< "Case #" << cnti << ": " ;
		while(a[22]>0)
		{
			c[k]='2';
						a[19]--;a[22]--; a[14]--;
			k++;
		}
		while(a[20]>0)
		{
			c[k]='4';
				a[5]--;a[20]--;a[17]--; a[14]--;
				k++;
				
		}
		while(a[23]>0)
		{
			c[k]='6';
				a[23]--;a[8]--;a[18]--;
				k++;
				
		}
		while(a[6]>0)
		{
			c[k]='8';
			a[8]--;a[4]--;a[6]--; a[7]--;a[19]--;
			k++;
		}
		while(a[25]!=0 && a[4]!=0 && a[17]!=0 && a[14]!=0)
		{
		//	cout<<"0";
			c[k]='0';
			a[25]--;a[4]--;a[17]--; a[14]--;
			k++;
		}
		while(a[13]!=0 && a[4]!=0  && a[14]!=0)
		{
		//	cout<<"1";
			c[k]='1';
			a[13]--;a[4]--; a[14]--;
		k++;}
		while(a[19]!=0 && a[22]!=0  && a[14]!=0)
		{
		//	cout<<"2";
			c[k]='2';
			a[19]--;a[22]--; a[14]--;
		k++;}
		while(a[19]!=0 && a[7]!=0 && a[17]!=0 && a[4]>1)
		{
		//	cout<<"3";
			c[k]='3';
			a[19]--;a[7]--;a[17]--; a[4]-=2;
		k++;}
		while(a[5]!=0 && a[20]!=0 && a[17]!=0 && a[14]!=0)
		{
		//	cout<<"4";
			c[k]='4';
			a[5]--;a[20]--;a[17]--; a[14]--;
		k++;}
			while(a[5]!=0 && a[8]!=0 && a[21]!=0 && a[4]!=0)
		{
		//	cout<<"5";
			c[k]='5';
			a[5]--;a[8]--;a[21]--; a[4]--;
		k++;}
			while(a[18]!=0 && a[8]!=0 && a[23]!=0)
		{
		//	cout<<"6";
			c[k]='6';
			a[23]--;a[8]--;a[18]--;
		k++;}
			while(a[13]!=0 && a[4]>1 && a[18]!=0 && a[21]!=0)
		{
		//	cout<<"7";
			c[k]='7';
			a[13]--;a[4]-=2;a[18]--; a[21]--;
		k++;}
			while(a[8]!=0 && a[4]!=0 && a[6]!=0 && a[7]!=0 && a[19]!=0)
		{
		//	cout<<"8";
			c[k]='8';
			a[8]--;a[4]--;a[6]--; a[7]--;a[19]--;
		k++;}
			while(a[8]!=0 && a[4]!=0 && a[13]>1 )
		{
		//	cout<<"9";
			c[k]='9';
			a[8]--;a[4]--;a[13]-=2; 
		k++;}
		 //ofs<< "Case #" << cnti << ": " <<maxi;
		 sort(c,c+k);
		 rep(i,k)
		 ofs<<c[i];
		 
		ofs<<endl;
	     //cout << "Case #" << cnt << ": " << ans << endl;
	       
	     cnti++; 
 	   }
}
