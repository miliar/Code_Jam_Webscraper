#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int t,n,i=1,h,p,s;
    bool digit[12]={false},f=false,sid=true;
    cin>>t;
    for(int j=0;j<=9;j++)
    	digit[j]=false;
    for(int g=0;g<t;g++)
    {
    	cin>>n;
  		if(n==0)
  			cout<<"Case #"<<g+1<<": INSOMNIA"<<endl;
  		else
  		{	i=1;f=false,sid=true;
  			for(int j=0;j<=9;j++)
    		digit[j]=false;
    		while(1)
    		{	
    			s=n*i;
    			p=n*i;
    			while(s!=0)
    			{
    				h=s%10;
    				digit[h]=true;
    				s=s/10;
    			}
    			//for(int j=0;j<=9;j++)
    			sid=true;	//cout<<j<<" "<<digit[j]<<" "<<endl;
    			for(int j=0;j<=9;j++)
    			{
    				if(digit[j]==false)
    					{
    						sid=false;
    						break;
    					}
    			}
    			if(sid==true)
    			{
    				cout<<"Case #"<<g+1<<": "<<p<<endl;
    				break;
    			}
    			
    			else i++;
    		}

    	}

    }
    return 0;
}