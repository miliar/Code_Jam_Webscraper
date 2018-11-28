#include <iostream>
using namespace std;

int main() {
	// your code goes here
//	cin>>t;
	long long q=1,t,temp,temp1,arr[10000],i,j,sum,d;
	cin>>t;
	while(t--)
	{
		temp=0;
		cin>>d;
		for(i=0;i<d;i++)
		{
			cin>>arr[i];
			temp=max(temp,arr[i]);
		}
		temp1=temp;
		for(i=1;i<=temp;i++)
		{
			sum=i;
			for(j=0;j<d;j++)
			{
				if( arr[j] > i ) 
				{  
                    if( arr[j]%i == 0 )  
                        sum=sum+(arr[j]/i-1) ;  
                    else  
                        sum =sum+ (arr[j]/i) ; 
				}
			}
			temp1 = min(temp1,sum) ; 
			}
		
		cout<<"Case #"<<q++<<": "<<temp1<<endl;
	}
	return 0;
}