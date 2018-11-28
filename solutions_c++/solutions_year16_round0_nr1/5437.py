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
bool f[10], bol;
LL n, m, k, i, j, t, x;
main(){
	   freopen("A.in","r",stdin);
	   freopen("A.out","w",stdout);
	   cin>>t;
	   for(i=1;i<=t;i++)
	    {
	     cin>>n;
	     memset(f,0,sizeof(f));
	     if(n==0){cout<<"Case #"<<i<<": INSOMNIA\n";continue;}
	     x=1;
		 while(true)
	      {
	       m=x*n;	
	       while(m)
		    {
		     f[m%10]=1;
			 m/=10;	  
			}
		   bol=true;	
		   for(j=0;j<=9;j++)if(!f[j])bol=false;
		   if(bol){cout<<"Case #"<<i<<": "<<x*n<<endl;break;}
		   x++;
		  }
	    }
       }

