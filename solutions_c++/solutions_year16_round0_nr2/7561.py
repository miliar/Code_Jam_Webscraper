#include <bits/stdc++.h>
#define max 1000000

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    
  	freopen("B-large.in","r",stdin);
	freopen("output_large.out","w",stdout);
    
	int t,u=0;
	cin>>t;
	for(int u=1;u<=t;u++){
	    string str;
	    cin>>str;
	    int c=0,k=0,l;
	    l=str.length();
	    
	    for(int i=0;i<l;i++){
	        
	        string r;
	        int k=0;
	        
	       	if(str[i]=='-'){
	       		
	       		if(!i)
	       			c++;
	       		else
	       			c+=2;
	       		
	       		int j=l-1,m;
	       		for(;j>=0;j--){
	       			if(str[j]=='-')
						break;	
	       			k++;
				}
				m=j+1;
				for(int p=j;p>=0;p--){
					
					if(str[p]=='-'){
						k++;	r+='+';
					}
					else
						r+='-';
				}
				
				for(;m<l;m++)
					r+='+';
			
	       		str=r;
	       		i=-1;
			} 
	        
	        else
	            str[i]='-';
	      
	      	 if(k==l)
	            break;
	        
	    }
	    cout<<"Case #"<<u<<": ";
	    cout<<c<<endl;
	    
	}
	
	return 0;
}
