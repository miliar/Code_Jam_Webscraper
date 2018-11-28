#include <iostream>
#include <cstring>
using namespace std;

int main() {
	int T,j,k,len,cpy,t;
	string s,a;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
	  cin>>s;
	  k=0;
	  j=1;
	  a[0]=s[0];
	  len=s.length();
	  cpy=len;
	  t=len;
	  
	  
	  while(len--)
	  {
    	  
    	  if(s[j]>=a[0])
    	  {
    	    
            	    t=cpy;
            	   
            	    while(t)
            	    {
            	    a[t-1]=a[t-2];
            	    t--;
            	    }
            	     if(t==0)
            	    {
            	    a[0]=s[j];
            	    }
    	    
    	    k++;
    	    j++;
    	    
    	  }
    	  else{
    	      a[k+1]=s[j];
    	      k++;
    	      j++;
    	      
    	  }
	  }
	  cout<<"Case #"<<i<<": ";
	 for(int z=0;z<cpy;z++)
	 {
	     cout<<a[z];
	     a[z]=0;
	 }
	 cout<<endl;  
	}
	
	
	
	return 0;
}
