#include<iostream>
using namespace std;
#include<stdio.h>
#include<set>
int  main()
 { int t,n,i,j,x,c,p,a,te;
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  
  set<int> s;
 	cin>>t;
 	for(te=1;te<=t;te++)
 	  {cin>>a;
 	  s.clear();
 	   for(i=0;i<4;i++)
 	     {for(j=0;j<4;j++)
 	        {
 	     	 cin>>x;
		 	 if(i==a-1)
 	      		  s.insert(x);
 	        }
		  
		  }
		  c=0;p=0;
		  cin>>a;
		  for(i=0;i<4;i++)
 	        {for(j=0;j<4;j++)
 	          {
 	         	 cin>>x;
		     	 if(i==a-1 && s.find(x)!=s.end())
 	      		  {c++;
 	      		   p=x;
 	      		   //s.insert(x);
 	      	      }
 	          }
		  
		    }
		 if(c==0)
		   cout<<"Case #"<<te<<": Volunteer cheated!"<<endl;
		 else if(c>1)
		   cout<<"Case #"<<te<<": Bad magician!"<<endl;
	 else
		   cout<<"Case #"<<te<<": "<<p<<endl;
 	  }
 	
 }
