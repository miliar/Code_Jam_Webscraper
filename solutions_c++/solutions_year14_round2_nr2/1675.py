#include<iostream>
using namespace std;
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<vector>
#include<stdio.h>
int main()
 {
 	char s[105];
 freopen("in.txt","r",stdin);
 	freopen("out.txt","w",stdout);
 	
 	int t,n,tes,flag;
 	cin>>t;
 	long long a,b,k,i,j,count;
 	for(tes=1;tes<=t;tes++)
 	  {
 	  	
 	  	cin>>a>>b>>k;
 	  	count=a*b;
		   //count=a+b-1;
 	  	
 	  	for(i=0;i<a;i++)
 	      {for(j=0;j<b;j++)
 	         {
 	         if( (i&j) >=k)
 	            {//cout<<i<<" "<<j<<endl;
 	            count--;
 	            }
 	          //  cout<<i<<" "<<j<<" "<< (i&j) <<endl;
 	        }
 	      }
 	  	cout<<"Case #"<<tes<<": "<<count<<endl;
 	  	
 	  	
 	  }
 	
 	
 	
 }
