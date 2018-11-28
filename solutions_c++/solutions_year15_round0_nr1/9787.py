#include <iostream>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	  {
	  	
	  	int s;
	  	 string name;
	  	   cin>>s>>name;
	  	   long long int sum=0;
	  	   int res=0;
	  	   int temp=0;
	  	   sum=name[0]-'0';
	  	   //cout<<sum<<" ";
	  	   for(int i=1;i<name.size();i++)
	  	    {  
	  	    	       if(i>sum)
	  	    	          {res=i-sum;
	  	    	          temp+=res;
	  	    	          
	  	    	          sum+=res;
	  	    	          }
	  	    	          
	  	    	          
	  	    	     (sum=sum+name[i]-'0');
	  	    	     //cout<<sum<<" ";
	  	    	      
	  	    	          
	  	    }
	  	    	 cout<<"Case #"<<t<<": "<<temp<<endl;       
	  	    	
	  	    	
	  	    	
	  	    }
}
	  	       
	  	   
	  	