#include <iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int k=1;k<=T;k++)
    {
    	int c1,n=0,x,a;
    	cin>>c1;
    	for(int i=0;i<4;i++)
    	{
    		for(int j=0;j<4;j++)
   			 {
    			cin>>a;
    			if(c1-1==i)
    			{	
    				x=1<<a;
    				n=n|x;
    			}
     
    		}
    	}
     
    	int c2,b=0,s;
    	cin>>c2;
    	
    	for(int i=0;i<4;i++)
    	{
   			for(int j=0;j<4;j++)
    		{
    			cin>>a;
    			if(c2-1==i)
    			{
    				
    				x=1<<a;
    				if((n&x)!=0)
    					{
    						b++; 
    						if(b==1)
    							s=a;
    					}
    			}
    		}
    		
   		}
    if(b==0)
    cout<<"Case #"<<k<<": Volunteer cheated!";
    else if(b==1)
    cout<<"Case #"<<k<<": "<<s;
    else
    cout<<"Case #"<<k<<": Bad magician!";
    cout<<endl;
    }
     
    return 0;
}
