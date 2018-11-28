#include<bits/stdc++.h>
using namespace std;
int getset(int hash[])
{
	long int i;
	
	for(i=0;i<10;i++)
	{
		if(hash[i]==0)
		 return 1;
	}
	
	return 0;
}


int main()
{

    long int t,n,i,temp,l=1;;
    
	//freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    
    while(t--)
    {
    	cin>>n;
    	cout<<"Case #"<<l<<": "; 
    	l++;
    	if(n==0)
    	cout<<"INSOMNIA\n";
		else{		int hash[10]={0};
		    	i=1;
		    	while(getset(hash))
		    	{
		    		temp=i*n;
		    		i++;
		    		//cout<<temp<<" ";
		    		while(temp>0)
		    		{
		    			hash[temp%10]=1;
		    			temp=temp/10;
		    			
		    		}
		    		
		    	
		    		
		    	}
		    	
		    	cout<<(i-1)*n<<"\n";
    	}
    	
    }

		  return 0;
}
