#include <iostream>
using namespace std;
int main() 
{
	int i,c,n=0,temp,rem,j,m,x,t,cas=0,new_n,z;
	cin>>t;
	for(z=0;z<t;z++)
	{
	   cin>>n;
	   int arr[10]={0,1,2,3,4,5,6,7,8,9};
	   temp=0;
	   c=10;
	   m=0;
	    cas++;
    	x=n;
	    if(n!=0)
	    {
	        while(c!=0)
    	    {
	            temp=n;
	            //cout<<temp<<" ";
	            while(temp!=0)
	            {
	                rem=temp%10;
	                temp=temp/10;
	                for(i=0;i<c;i++)
	                {
	                    if(arr[i]==rem)
	                    {
	                        for(j=i;j<c;j++)
	                        {
	                            arr[j]=arr[j+1];
	                        }
	                        c--;
	                    }
	                }
	            }
	            m++;
	            if(c!=0)
	            {
	            //new_n=n;    
	            n=x*(m+1);
	            }
    	    }
	    cout<<"Case #"<<cas<<": "<<n<<"\n";
	}
	else
	{
	   cout<<"Case #"<<cas<<":"<<" INSOMNIA\n";
	}
	}
	return 0;
}
