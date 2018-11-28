#include<iostream>

using namespace std;



int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	
	int t,c;
	
	cin>>t;
	c=t;
	
	while(t--)
	{
		int n;
		
		cin>>n;
		
		if(n==0)
		cout<<"Case #"<<c-t<<": "<<"INSOMNIA"<<endl;
		
		else {
			
				int arr[10]={0},temp,i,j;
				
				for(i=1;;i++)
				{
					temp=n*i;
					
					while(temp)
					{
						arr[temp%10]=1;
						temp/=10;
					}
					
					
					for(j=0;j<10;j++)
					if(arr[j]==0)
					break;
					
					if(j==10)
					break;
					
				}
				
				cout<<"Case #"<<c-t<<": "<<n*i<<endl;
		}
	}
}
