#include <iostream>
#include <math.h>
#include <algorithm>
#include <stdio.h>
using namespace std;

int T,t1,a[9][9],n,x,m,m1,i,j;

string s,s1,ans;

int davamushaot(int x,int y)
{
	if (x==0) return y;
	if (x<0 && y<0) return davamushaot(-x,-y);
	if (x*y<0) return (-davamushaot( abs(x), abs(y) ) ); else
	           return a[x][y];  
}

main()
{
	
	 freopen ("input.txt","r",stdin);
	 freopen ("output.txt","w",stdout);
	 
	 cin>>T;
	   t1=T;
	   
	   a[1][1]=1; a[1][2]=2;  a[1][3]=3;  a[1][4]=4;
	   a[2][1]=2; a[2][2]=-1; a[2][3]=4;  a[2][4]=-3;
	   a[3][1]=3; a[3][2]=-4; a[3][3]=-1; a[3][4]=2;
	   a[4][1]=4; a[4][2]=3;  a[4][3]=-2; a[4][4]=-1;
	   
	   
	     while (T--)
	      {
             cin>>n>>x; x--;
			  cin>>s; s1=s; ans="YES";
			  
			  while (x--)   s+=s1;
	
			   n=s.size();
			  
			  m=0;
			  for (i=0;i<s.size();i++)
			   {
			  if (s[i]=='i') m1=2; else
			  if (s[i]=='j') m1=3; else 
			                 m1=4;
			        
			        m=davamushaot(m,m1);
			   	
				 }  
			   if (m!=-1) ans="NO"; 
			   
			 m=0;
			  for (i=0;i<s.size();i++)
			   {
			    if (s[i]=='i') m1=2; else
			    if (s[i]=='j') m1=3; else 
			                   m1=4;
			        
			        m=davamushaot(m,m1);
			     if (m==2) break; 	
				 }  
			  if (i==s.size()) ans="NO";
			 
			 /**/
		     m=0;
			  for (j=n-1;j>=0;j--)
			   {
			  if (s[j]=='i') m1=2; else
			  if (s[n]=='j') m1=3; else 
			                 m1=4;
			        
			        m=davamushaot(m,m1);
			     if (m==4) break; 	
				 }  
			  if (j==-1) ans="NO";
			     if (i>=j) ans="NO";    
			    
				
				 
 			   cout<<"Case #"<<t1-T<<": "<<ans<<endl;
 		  }
	  
	
}
