#include<bits/stdc++.h>
using namespace std;
typedef long long int lli;
int flip(string &s,int l,int r)
 {
 	  while(l<r)
 	    {
 	    	char temp=s[l];
 	    	 if(s[r]=='+') s[l]='-';
 	    	 else s[l]='+';
 	    	 if(temp=='-') s[r]='+';
 	    	 else s[r]='-';
 	    	 l++;
 	    	 r--;
 	   	
		}
		if(l==r)
		 {
		 	 if(s[l]=='-') s[l]='+';
		 	 else s[r]='-';
		 }
 }
 
 
int main()
{
	
	   freopen("abc.txt","r",stdin);
	   freopen("pqr.txt","w",stdout);
	 int n;
	  int cas=1;
	 int t;
	  cin>>t;
	  while(t--)
	   {
	   	 cout<<"Case #"<<cas++<<": ";
	   	  string  s;
	   	   cin>>s;
	   	     int len=s.length();
	   	    int r=len-1;
	   	    int l=0;
	   	    int count=0;
	   	while(r>=0) 
	   	    {
	   	    	 if(s[r]=='+')
	   	    	  {
	   	    	  	 r--;
	   	    	  	  continue;
					 }
					 else
					 {
					 	l=0;
					 	 if(s[0]=='-')
					 	  {
					 	  	 count++;
					 	  	 flip(s,l,r);
					 	  	 
						   }
						   else
						   {
						   	 count++;
						   	   while(l<=r && s[l]=='+')
						   	       {
						   	    	 s[l]='-';
						   	    	 l++;
								   }
								   
								   count++;
								   flip(s,0,r);
						   }
					 }
	   	 	  
			}
	 	cout<<count<<endl;
	   }
}
