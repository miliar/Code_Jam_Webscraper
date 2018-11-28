#include <bits/stdc++.h>
#include<stdio.h>
using namespace std;
#define pii pair<long long,long long>
#define F(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define RF(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define debug(x) cout << #x << " = " << x << endl
#define INF 1000000009
#define mod 1000000007
struct ab
{
    float a;
    char b;
    
};
bool cmp( ab x, ab y){
    
      return x.a > y.a;
}
int main() {
	// your code goes here
	ll count=0;
	ll n;
	ll a;
	ll sum;
	ll k;
	cin>>n;
	while(n--)
	{
	    count++;
	    cin>>a;
	    ab imp[a];
	    k=65;
	    for(int i=0;i<a;i++)
	    {
	        cin>>imp[i].a;
	        imp[i].b=(char)k;
	        k++;
	    }
	    cout<<"Case #"<<count<<": ";
	    while(1)
	    {sum=0;
	 
	 
	            sort(imp,imp+a,cmp);
	            
	            if(imp[0].a==0)
	            break;
	            imp[0].a--;
	            cout<<imp[0].b;
	            for(int i=0;i<a;i++)
	            sum+=imp[i].a;
	   
	            
	             if((imp[0].a)/sum >0.5)
	            {
	                
	                imp[0].a--;
	                cout<<imp[0].b;
	            }
	            else if((imp[1].a)/sum >0.5){
	             imp[1].a--;
	             cout<<imp[1].b;
	            }
	    cout<<" ";
	}
	cout<<"\n";
	}
	return 0;
}
