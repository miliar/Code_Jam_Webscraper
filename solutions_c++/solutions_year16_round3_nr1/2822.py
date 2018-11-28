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
	ll t,n,cnti=1,m,ss;
	ifs>>t;
	//ifs>>t;
	while(t--)
	{
			ofs<< "Case #" << cnti << ": " ;
		    //ifs>>n;
		    ifs>>n;
		    //ll a[n];
		    vector<pll>vv;
		    //map<ll,ll>::iterator it,it2;
		    rep(i,n)
		    {
		    	//ifs>>m;
		    	ifs>>m;
		        vv.pb(mb(m,i));
			}
			sort(vv.begin(),vv.end());
			//rep(i,vv.size())
			//cout<<vv[i].F<<" "<<vv[i].S<<endl;
			//cout<<vv.size()<<endl;
			while(vv.size()>0)
			{
				ll ff;
					ll tt=vv[vv.size()-1].F;
				if(vv.size()>=2)
			    ff=vv[vv.size()-2].F;
				if(((tt-ff)==0) && vv.size()==2)
				{
					//cout<<"yt"<<endl;
					//it2=st.begin();
					if(tt==1)
					{
						//cout<<"kir"<<endl;
						//rep(i,vv.size())
						//cout<<vv[i].F<<" "<<vv[i].S<<endl;
					char c1,c2;
					c1='A';
					c2='A';
					c1 =(int)c1 + vv[1].S;
					c2 = (int)c2 + vv[0].S;
					ofs<<c1<<c2<<" ";
					vv.pop_back();
					vv.pop_back();
					//st.erase(it2);
					
				    }
				    else
				    {
				    //	cout<<"vvvv"<<endl;
				     ll p,q,r,s;	
				     char c1,c2;
					 c1='A';
					 c2='A';
					 c1 =(int)c1 + vv[1].S;
					 c2 = (int)c2 + vv[0].S;
					 ofs<<c1<<c2<<" ";
				  p=vv[vv.size()-1].F-1;
				  q=vv[vv.size()-1].S;
				  r=vv[vv.size()-2].F-1;
				  s=vv[vv.size()-2].S;
			      vv.pop_back();
			      vv.pop_back();
			      if(p==0 && r==0)
			      continue;
			      else
			      {
			      	if(p!=0 && r==0)
	                vv.pb(mb(p,q));
	                else if(p==0 && r!=0)
	                vv.pb(mb(r,s));
	                else
	                {
	                	 vv.pb(mb(p,q));
	                	 vv.pb(mb(r,s));
					}
	               sort(vv.begin(),vv.end());
	              }
				    	
					}
				}
				else
				{
					//cout<<"vai"<<endl;
				 char c;
				 c='A';
				 c=(int)c+vv[vv.size()-1].S;
				 ofs<<c<<" ";
				 ll p=vv[vv.size()-1].F-1;
				 ll q=vv[vv.size()-1].S;
			     vv.pop_back();
			     if(p==0)
			     continue;
			     else
	             vv.pb(mb(p,q));
	             sort(vv.begin(),vv.end());
			   }
		//ofs<< "Case #" << cnti << ": " ;
         }
		 
		ofs<<endl;
		//cout<<endl;
	     //cout << "Case #" << cnt << ": " << ans << endl;
	       
	     cnti++; 
 	   }
}
