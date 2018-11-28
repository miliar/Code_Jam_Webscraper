#include<bits/stdc++.h>
#define ll long long int
#define s(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define w(t) while(t--)
#define f(i,n) for(i=0;i<n;i++)
#define fd(i,n) for(i=n-1;i>=0;i--)
#define p(a) printf("%d",a)
#define pl(a) printf("%lld",a)
#define ps(a) printf("%s",a)
#define pc(a) printf("%c",a)
#define ent printf("\n")
#define maxn 100000
#define mod 1000000007
#define po(a,b) (long long int)pow((double)(a),(double)(b))
#define abs(a) (long long int)abs((double)(a))
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
#define sz(a) (long long int)((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define se second
#define fi first
using namespace std;
typedef pair <ll,ll> pii;
vector <pii> vec;
vector <char> vec1,vec2;
int main()
{ 
  freopen("inp.txt","r",stdin);

freopen("opt.txt","w",stdout);
	ll t,n,i,x,t1;
	sl(t);
	 t1=t;
	 w(t)
	 {  
	    vec1.clear();
	 	  vec2.clear();
	 	   vec.clear();
	 	sl(n);
	 	 f(i,n){
	 	   sl(x);
	 	    vec.pb(mp(x,i));
	 	     
			 }
	 	   sort(vec.begin(),vec.begin()+n);
	 	   for(i=n-1;i>=0;i--)
	 	    {
	 	    	if(vec1.size()<=vec2.size())
	 	    	for(int j=0;j<vec[i].fi;j++)
	 	    	{
	 	    		vec1.pb(((char)vec[i].se+97));
	 	    	}
	 	    	else
	 	    	for(int j=0;j<vec[i].fi;j++)
	 	    	{
	 	    		vec2.pb((char)(vec[i].se+97));
	 	    	}
	 	    }
	 	    /*f(i,vec1.size())cout<<vec1[i];
	 	    ent;
	 	    f(i,vec2.size())cout<<vec2[i];ent;*/
	 	    if(vec1.size()>vec2.size())
	 	    { char c=vec1[vec1.size()-1];
	 	    	while(vec1.size()>vec2.size())
	 	    	{
	 	    		vec2.pb(c);
	 	    		vec1.pop_back();
	 	    	}
	 	    }
	 	    else if(vec2.size()>vec1.size())
	 	    { char c=vec2[vec2.size()-1];
	 	    	while(vec2.size()>vec1.size())
	 	    	{
	 	    		vec1.pb(c);
	 	    		vec2.pop_back();
	 	    	}
	 	    }
	 	    cout<<"Case #"<<(t1-t)<<":"<<" ";
	 	    if(vec1.size()>vec2.size()){int l=vec1.size();
			 cout<<vec1[l-1]<<" ";
	 	      //vec1.pop_back();
	 	    }
	 	    else if(vec2.size()>vec1.size()){int l=vec2.size();
			 cout<<vec2[l-1]<<" ";
	 	      //vec2.pop_back();
	 	    }
	 	    //cout<<"Case #"<<(t1-t)<<":"<<" ";
	 	    for(i=min(vec1.size(),vec2.size())-1;i>=0;i--)cout<<vec1[i]<<vec2[i]<<" ";
	 	    ent;
	 }
}
