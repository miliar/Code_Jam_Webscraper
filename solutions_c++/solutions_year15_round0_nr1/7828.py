#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
using namespace std;
/*Scan/Print Macros*/
#define si(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define pi(n) printf("%d",n)
#define pl(n) printf("%lld",n)
#define nl printf("\n")
#define sp printf(" ")
/*For Macros*/
#define fa(i,n) for(i=0;i<n;i++)
#define fab(i,a,b) for(i=a;i<=b;i++)
#define fabn(i,a,b) for(i=a;i<=b;i++)
/*STL Macros*/
#define pb push_back
#define f first
#define s second
#define sz size()
#define all(a) a.begin(),a.end()
#define fill(x,c) memset(x,c,sizeof(x))
typedef long long ll;
/*Const Macros*/
const int M=1e9+7;

int main()
{
	ll smax;;
    ll i,j,k,t,n,m,ans;
    sl(t);
    //char jl;
    //cin>>jl;
    ll ctr = 0;
    while(t--)
    {
    	ctr +=1;
    	ll a[1500]={0};
    	cin>>smax;
    	char junk;
    	//cin>>junk;
    	//cout<<junk<<endl;
    	fa(i,smax+1)
    	{
    		cin>>junk;
    		ll tmp = junk-'0';
    		a[i] = tmp;
    	}
    	// pl(smax);nl;
    	// fa(i,smax+1){
    	// 	pl(a[i]);sp;
    	// }
    	// nl;
    	ans = 0;
    	ll cum = a[0];
    	for(i=1;i<=smax;i++)
    	{
    		ll req = i;
    		if(cum>=req)
    		{
    			cum += a[i];
    		}
    		else
    		{
    			//cout<<"add"<<endl;
    			ans += (req-cum);
    			cum += (req-cum);
    			cum += a[i];
    		}
    	}
    	cout<<"Case #"<<ctr<<": "<<ans<<endl;

    }
    return 0;
}