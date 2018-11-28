#include<iostream>
using namespace std;
#include <fstream>

int main()
{
	ofstream output;
    ifstream input;
    input.open ("D-large (1).in");
    int x,n;
    double t,a[1000],b[1000],a0[1000],b0[1000],z[1000],y[1000];
    input>>x;
    for(int a1=0;a1<x;a1++)
    {
    	
    	input>>n;
    	y[a1]=n;
    	z[a1]=0;
    
    	for(int i=0;i<n;i++)
    	{
    		input>>a[i];
    		a0[i]=a[i];
    		
    	}
    	
    	for(int i=0;i<n;i++)
    	{
    		input>>b[i];
    		b0[i]=b[i];
    	
    	}
    	
    	for(int i=0;i<n;i++)
    	{
    		for(int j =0;j<n;j++)
    		{
			 if(a[i]>a[j])
    		  {
    		  	t = a[j];
    		  	a[j]=a[i];a0[j]=a[i];
    		  	a[i]=t;a0[i]=t;
    		  }
    		 if(b[i]>b[j])
    		  {
    		  	t = b[j];
    		  	b[j]=b[i];b0[j]=b[i];
    		  	b[i]=t;b0[i]=t;
    		  }
    	    }
			
	 	}


    	for(int i=(n-1);i>=0;i--)
    	{
    		for(int j=(n-1);j>=0;j--)
    		{
    			if((a[i]<b[j]))
    			{
    				y[a1]--;
    				a[i]=0;
    				b[j]=0;
    				break;
    				
    			}

    	    }
        }
       	   

    	for(int i=(n-1);i>=0;i--)
    	{
    		for(int j=(n-1);j>=0;j--)
    		{
    			if((b0[i]<a0[j]))
    			{   
				    z[a1]++;
    				b0[i]=0;
    				a0[j]=0;
    				break;
    				
    			}
    	   }
        }   
	}
	output.open ("output.txt");
       for(int k=0; k<x;k++)
       {
        output<<"Case #"<<k+1<<": "<<z[k]<<" "<<y[k]<<endl;
       
       }
       
       output.close();
       return 0;
       
    
}
