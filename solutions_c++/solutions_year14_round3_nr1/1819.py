#include<bits/stdc++.h>
#define pb push_back
#define pii std::pair< int,int >
#define p(i,j) std::pair< i, j>
#define lli long long int
#define v(x) vector< x >
#define vv(x) vector< vector< x > >
#define mp make_pair
#define fu(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define max(a,b) (a>b)?a:b 
#define ain(a,i) for(int i=0;i<a.size();i++) {cin>>a[i];}
#define aout(a,i,x) for(int i=0;i<a.size();i++) {cout<<a[i]<<x;}
#define numt(i,t) int t;cin>>t;for(int i=1;i<=t;i++)
#define tout(i) cout<<"Case #"<<i<<": "
using namespace std;
lli gcd(lli a,lli b)
{
	if(b==0)
	{
		return a;
	}
	else if(a%b==0)
	{
		return b;
	}
	else{
		return gcd(b,a%b);
	}
}
//cout<<"Case #"<<i<<": ";
int main()
{
	numt(ii,t){
		lli p,q;
		scanf("%lld/%lld",&p,&q);
		
		//cout<<p<<" "<<q<<endl;
		//tout(ii)<<p<<" "<<q<<endl;
		lli gc=gcd(q,p);
		p=p/gc;
		q=q/gc;
		lli j=0;
		//cout<<gc<<" "<<p<<" "<<q<<endl;
		while(pow(2,j)<q)
		{
			j++;
			//cout<<pow(2,j)<<endl;
		}
		if(pow(2,j)==q)
		{
					lli x=q;
					lli jj=0;
				while(x>0)
				{
					if(x<=p)
					{
						tout(ii)<<jj<<endl;
						break;
					}
					x=x/2;
					jj++;
				}
		}
		else{
			tout(ii)<<"impossible"<<endl;
		}
	}
	return 0;
}
