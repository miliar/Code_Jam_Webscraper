	#include<iostream>
	#include<vector>
	using namespace std;
	#include<cstdio>
	#define pb push_back
	vector<int>m;
	void pre()
          { 
	  
	   m.pb(1);
	   m.pb(4);
	   m.pb(9);
	   m.pb(121);
	   m.pb(484);
	}
	int main()
	{
	   int key=0;
	   if(key==0) key==1;
	  freopen("palins.in","r",stdin);
	  freopen("palins.out","w",stdout);
	  int test;
	  pre();
	  cin>>test;
	   
	   for(int it=1;it<=test;it++)
	   {
	         int x,y;
	         cin>>x>>y;
	          
	          int res=0;
	          for(int j=0;j<m.size();j++)
	          {
	                if(m[j]>=x && m[j]<=y)
	                res++;
	          }
	          cout<<"Case #"<<it<<": "<<res<<endl;
	   }
	}
