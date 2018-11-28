#include<iostream>

using namespace std;

int main()
{
	int T;
	long long unsigned int n;
	long unsigned int N;
	
	cin>>T;
	int t=0;
	
	
	while(t!=T)
	{
		int A[]={0,0,0,0,0,0,0,0,0,0};
		int flag=1;      //Reverse flag
		
		cin>>N;
		n=N;
		
		if(N==0)
		   	cout<<"Case #"<<t+1<<": INSOMNIA"<<endl;
		else
		{
		
		  int k=1;
		   
		  do
		  {
		  	
		  	n=N*k;
		  
		    k++;
		    
		    do 
		    {
         	    int digit = n % 10;
        	    A[digit]=1;
            	n /= 10;
		    } while (n > 0);
		  
		    flag=1;
		
		    for(int i=0;i<10;i++)
	    	{
	    		flag*=A[i];
	    	
		    }
		   
		    
	      }while(flag!=1);
	      
	      k--;
	    
	     cout<<"Case #"<<t+1<<": "<<N*k<<endl;			
		 
	 
	    } 
		
		t++; 
	}
	
	
	return 0;
}
