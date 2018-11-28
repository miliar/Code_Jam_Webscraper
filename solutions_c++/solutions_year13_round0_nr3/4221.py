	#include<iostream>
	#include<vector>
	#include<cstdio>
	#include<algorithm>
	#include<string>
	#include<cstdlib>
	#include<sstream>
	#include<cmath>
	#define ll long long
	using namespace std;
		string tostr(ll x)
{ stringstream ss; ss << x; return ss.str(); }
ll toint(string &s)   
{ stringstream ss; ss << s; long long x; ss >> x; return x; }
	vector<ll> a;
	bool checknines(string s)
	{
	      for(int i=0;i<s.length();i++)
	      {
                     if(s[i]!='9') return false;
	      }
	      return true;
	}
	ll next1(string s)
	{
	     int l=s.length();
	     ll num=toint(s);
	     return num+2;
	}
	bool ispal(ll n)
	{
	    string s=tostr(n);
	    int st=0;
	    
	    int e=s.length()-1;
	    while(st<s.length()/2)
	    {
	          if(s[st]!=s[e]) return false;
	          st++;
	          e--;
	    }
	    return true;
	}
	ll nextpal(ll n)
	{
	        string s=tostr(n);
	        if(checknines(s))
	        {
	            return next1(s);
	        }
	        int l=s.length();
	        int mid=l/2;
	        int end=(l%2) ? (l/2+1):l/2;
	        string left=s.substr(0,end);
	        string right=s.substr(end,l-end);
	        ll lefti=toint(left);
	        lefti++;
	        left=tostr(lefti);
	        if(l%2)
	        {
	            right=left.substr(0,left.length()-1);
	            
	        }
	        else
	        {
	           right=left.substr(0,left.length());
	        }
	        reverse(right.begin(),right.end());
	        s=left+right;
	        return toint(s);
           }
	bool is_sqr(ll n)
	{ 
	    double root=sqrt(n);
	    if(root==int(root))
	    {
	        return true;
	    }
	    return false;
	}
	int c=0;
	void solve()
	{
	       ll maxn=1000*10*1000;
	       
	        for(ll i=1;i<maxn;i=nextpal(i))
	        {
	           ll sq=i*i;
	           if(ispal(sq))
	           {
	              c++;
	             // cout<<c<<" "<<sq<<endl;
	               a.push_back(sq);
	           }
	          
	      
	        }
	        
	}
	int main()
	{
	
	  freopen("palins.in","r",stdin);
	  freopen("palins.out","w",stdout);
	  int test;
	  solve();
	  cin>>test;
	  //return 0; 
	   for(int it=1;it<=test;it++)
	   {
	         ll x,y;
	         cin>>x>>y;
	         int res=0;
	         for(int i=0;i<a.size();i++)
	         {
	               if(a[i]>=x && a[i]<=y)
	               {
	                    res++;
	               }
	         }
	        cout<<"Case #"<<it<<": "<<res<<endl;
	   }
	   return 0;
	}
