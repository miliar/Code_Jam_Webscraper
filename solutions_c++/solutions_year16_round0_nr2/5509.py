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
LL n, m, k, i, j, t, ind, res, x;
main(){
	   freopen("B.in","r",stdin);
	   freopen("B.out","w",stdout);
	   cin>>t;
	   for(i=1;i<=t;i++)
	    {
	     cin>>s; res=0; bool bol=false;
	     for(j=s.si-1;j>=0;j--)
	       if(bol==true && s[j]=='+')res++, bol=false;
	       else if(bol==false && s[j]=='-')res++, bol=true;
		   	
		 cout<<"Case #"<<i<<": "<<res<<"\n";
	    }
       }
//cout<<"Case #"<<i<<": INSOMNIA\n";
