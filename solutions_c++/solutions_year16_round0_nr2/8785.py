#include <iostream>
#include<cstring>
using namespace std;

int main() {
     int test,j,k,i,t,count,n;
     cin>>test;
	 string str;
	 for(t=1;t<=test;t++)
	 {
	  cin>>str;
	 n=str.size();
	  count=0;
	 while(true)
	 {
	   i=0;
	      if(str[i]=='-')
	       { while(str[i]=='-'&&i<n)
	          i++;
	          for(k=0;k<i;k++)
	              str[k]='+';
	             
	          count++;
	          }
	          
	     else
	         { 
	            for(j=0;j<n;j++)
	                { if(str[j]=='-') break;
	                }
	                if(j== n)
	                { break;}
	              
	                
	           while(str[i]=='+'&&i<n)
	              i++;
	          for(k=0;k<i;k++)
	            str[k]='-';
	            count++;
	         }
	          
	 } 
	 cout<<"Case #"<<t<<": "<<count<<endl;
	 
	 }
	 return 0;
}