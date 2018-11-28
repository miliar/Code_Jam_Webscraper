#include<iostream>

using namespace std;

int main()
{

    int test;
    cin>>test;
    for(int i=0;i<test;i++)
    {
	char a;
    long long int b,c,temp;
    cin>>b;
    cin>>a;
    cin>>c;
    long long int count=0;
    for(long long int k=b;k>=2;k--)
    {
	 if((b%k==0)&&(c%k==0))	
	 {
	 	b=b/k;
	 	c=c/k;
	 	break;
	 }
	 else
	 continue;
    }
    long long int flag=0;
    temp=c;
    while(temp>1)
    {
    	if(temp%(2)==1)
    	{flag=1;
    	break;
    	}
    	
    	temp=temp/2;
    }
    
    while(b<c)
    {
    	b=b*2;
    	
    	count++;
    }
    if(flag==1)
    cout<<"Case #"<<i+1<<": "<<"impossible\n";
    else
    cout<<"Case #"<<i+1<<": "<<count<<"\n";
    	
    }
    
    return 0;
    
}



 
 
      
         
     
            
