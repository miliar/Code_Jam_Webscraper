#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define N 1000001
#define hg ios_base::sync_with_stdio(0);cin.tie(0)
#define ff first
#define ss second
#define gcd __gcd
#define inf (1<<30)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pll pair<ll,ll>
#define bitcit __builtin_popcount
#define mset(x,y) memset(x,y,size(x))
#define INF 1e18
#define ll long long
#define endl "\n"

ll ex(ll a, ll b){
  ll result = 1;
  while (b){
    if (b%2==1){
      result= (result*a)%mod;
    }
    b /= 2;
    a= (a*a)%mod;
  }
  return result;
}

int main() {
    hg;
    int t,i,j,n,m,k=1;
    cin>>t;
    set< pair<int,char> > s;
    set< pair<int,char> >::iterator it1,it2;
    for(k=1;k<=t;k++)
    {
    	cin>>n;
    	int p;
    	for(i=0;i<n;i++)
        {   char pp;
        	cin>>p;
        	p=(-1)*p;
            pp=i+65;
        	s.insert(mp(p,pp));
        }
        cout<<"Case #"<<k<<": ";
        it1=s.begin();
        while(s.size()>1)
        {   it1=s.begin();
            if(it1==s.end())
            break;
        	it2=it1;
        	it2++;
        	if((abs((it1->ff))==abs((it2->ff))))
        	{
        		if(abs((it1->ff))!=1)
        		{
        		 cout<<it1->ss<<it2->ss<<" ";
        		char p1,p2;
        		int val1,val2;
        		p1=it1->ss;p2=it2->ss;
        		val1=abs(it1->ff);val2=abs(it2->ff);
        		s.erase(it1);s.erase(it2);
        		val1--;
        		val2--;
        		if(val1>0)
        		{   val1=-1*val1;
        			s.insert(mp(val1,p1));
        		}
        		if(val2>0)
        		{   val2=-1*val2;
        			s.insert(mp(val2,p2));
        		}
        	  }
        	  else
        	  {
        	  	if(s.size()>2)
        	  	{
        	  	cout<<it1->ss<<" ";
        		s.erase(it1);
        		
        	  	}
        	  	else
        	  	{
        	  		cout<<it1->ss<<it2->ss<<" ";
        	  		s.erase(it1);
        	  		s.erase(it2);
        	  	}
        	  }
        	}
        	else if((abs((it1->ff))-abs((it2->ff))==1))
        	{
        		cout<<it1->ss<<it2->ss<<" ";
        		char p1,p2;
        		int val1,val2;
        		p1=it1->ss;p2=it2->ss;
        		val1=abs(it1->ff);val2=abs(it2->ff);
        		s.erase(it1);s.erase(it2);
        		val1--;
        		val2--;
        		if(val1>0)
        		{   val1=-1*val1;
        			s.insert(mp(val1,p1));
        		}
        		if(val2>0)
        		{   val2=-1*val2;
        			s.insert(mp(val2,p2));
        		}
        		
        	}
        	else if((abs((it1->ff))-abs((it2->ff)))>=2)
        	{
        		cout<<it1->ss<<it1->ss<<" ";
        		int value;char cc;
        		value=abs(it1->ff);
        		cc=it1->ss;
        		value-=2;
        		s.erase(it1);
        		if(value>0)
        		{	
        	       value=(-1)*value;
        		   s.insert(mp(value,cc));
        		}
        	}
        
        }
        cout<<"\n";
    } 
	return 0;
}