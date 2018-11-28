#include <iostream>
#include<string.h>
using namespace std;

int main() {
	// your code goes here
	
	
	int t,j;
	cin>>t;
	j=0;
	while(t--)
	{char s[2003];
	    int a[100]={0};
	    
	    cin>>s;
	    int i,n;
	    n=strlen(s);
	    for(i=0;i<n;i++)
	    {
	        a[s[i]]+=1;
	        
	    }
	    j++;
	    cout<<"Case #"<<j<<": ";
while(a[90]>0)
	   {
	       a[90]--;a[79]--;
	       cout<<0;
	   }
	   
	   while((a[79]-a[87]-a[85])>0)
	   {
	       a[79]--;
	       cout<<1;
	   }
	   
	   while(a[87]>0)
	   {
	       a[87]--;a[84]--;
	       cout<<2;
	   }
	   
	   while((a[84]-a[71])>0)
	   {
	       a[84]--;
	       cout<<3;
	   }
	   
	   while(a[85]>0)
	   {
	       a[85]--;a[70]--;
	       cout<<4;
	   }
	   while(a[70]>0)
	   {
	       a[70]--;a[73]--;a[86]--;
	       cout<<5;
	   }
	   while(a[88]>0)
	   {
	       a[88]--;a[73]--;
	       cout<<6;
	   }
	   
	   while(a[86]>0)
	   {
	       a[86]--;
	       cout<<7;
	   }
	   
	   while(a[71]>0)
	   {
	       a[73]--;a[71]--;
	       cout<<8;
	   }
	   while(a[73]>0)
	   {
	       a[73]--;
	       cout<<9;
	   }
	   cout<<"\n";
	}
	return 0;
}

