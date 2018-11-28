#include<bits/stdc++.h>
using namespace std;
#define ll long long 
#define ull unsigned long long 
#define m(a,i,n) memset(a,i,n)
#define f(i,n) for(i=0;i<n;i++)
#define sc(a) scanf("%lld",&a)
#define vect_int vector<int>
#define pb(x) push_back(x)
#define lb lower_bound
#define ub upper_bound
#define pf(a) printf("%lld\n",a)
/*inline void Scan_f(int& a)
{
	char c = 0;
	while(c<33)
	c= getc(stdin);
	a = 0;
	while(c>33)
	{
		a = a*10 + c - '0';
		c = getc(stdin);
	}
}*//*
ll gcd(ll a,ll b)
{
	if(b == 0)
	{
	    return a;
	}
	else
	{
		return gcd(b, a % b);
	}
}*/
//map<pair<ll,ll>,ll>  :: iterator itr;
//M[make_pair(a,b)]++;
int main() { 
	// your code goes here
 	ios_base::sync_with_stdio(false);
 	ll t,n,i,j,q,k; 	
 	map <ll,ll> M;
 	vector<ll> v;
 	map <ll,ll> :: iterator it;
 	cin>>t;
 	for(k=1;k<=t;k++)
 	{
 		M.clear();
 		v.clear();
 		cin>>n;
 		f(i,2*n-1)
 		{
 			f(j,n)
 			{
 				cin>>q;
 				M[q]++;
// 				cout<<q<<" "<<M[q]<<endl;;
			}
		}
		for(it=M.begin();it!=M.end();it++)
		{
			if(it->second %2 ==1)
			v.pb(it->first);
		}
		sort(v.begin(),v.end());
		cout<<"Case #"<<k<<": ";
		f(i,v.size())
		cout<<v[i]<<" ";
		cout<<endl;
 	}
	
	return 0;
}
