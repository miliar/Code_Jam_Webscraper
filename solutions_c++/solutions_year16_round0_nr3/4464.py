#include <bits/stdc++.h>
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define UP upper_bound
#define LB lower_bound
#define LL long long 
#define Pi 3.14159265358
#define si size()
#define en end()
#define be begin()
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ii set<int>::iterator
#define Tree int ind, int L, int R
#define Left 2*ind,L,(L+R)/2
#define Right 2*ind+1,(L+R)/2+1,R
using namespace std;
string s;
bool bol;
vector < int > g;
vector < bool > v;
LL n, m, k, i, j, t, X, Y, cur, ind, res, x;
long long prime(long long x)
{
	for(long long i=2;i*i<=x;i++)
      if(x%i==0)return i;
    return 0;
}
main(){
	   freopen("C.in","r",stdin);
	   freopen("C.out","w",stdout);
	   cin>>t;
	   for(i=1;i<=t;i++)
	    {
	     cin>>n>>k;
	     cout<<"Case #"<<i<<":"<<endl;
	     for(i=(1<<(n-1))+1;i<(1<<(n));i+=2)
	      {bol=true; g.clear();
	       for(j=2;j<=10;j++)
	        {
		     X=i; cur=0; m=1;
		     for(int l=0;l<n;l++)
               cur=cur*j+(((1<<l)&i)?(1):(0));
			 Y=prime(cur);  
			 if(!Y){bol=false;break;} 
			 g.pb(Y);
		    }
		   int x=i; 
		   //cout<<bol<<endl;
		   //while(x)v.pb(x%2), x/=2;
			// for(j=v.si-1;j>=0;j--)cout<<v[j]<<" ";
			// system("pause");
		   if(bol)
		    {	
		     int x=i; 	
		     while(x)v.pb(x%2), x/=2;
			 for(j=v.si-1;j>=0;j--)cout<<v[j];cout<<" ";
			 for(j=0;j<g.si;j++)cout<<g[j]<<" ";
			 cout<<endl;
			 v.clear(); k--;
			 if(k==0)break; 	
			  }  
		  }
	    }
       }
//cout<<"Case #"<<i<<": INSOMNIA\n";
