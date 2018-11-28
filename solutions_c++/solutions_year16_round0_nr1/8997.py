#include <iostream>
using namespace std;
int arr[10];
int read(long n, int left) 
{
		
		
		long temp;
		while(n>0)
		{
			temp=n%10;
			if(arr[ temp]==0)
			{
				left--;
				arr[ temp]++;
			}
			n=n/10;
		}
		return left;
}

int main() 
{

	int t;
	cin>>t;
	long n;
	int i,left,in=1;
	while(in<=t)
	{
	cin>>n;
		if(n==0)
			cout<<"Case #"<<in<<": INSOMNIA"<<endl;
			
			else
			{
				i=1;
			
				for (int j = 0; j < 10; j++) {
					arr[j]=0;
				}
				left=10;
				while(left>0)
				{
					
					left =read(n*i,left);
					i++;
				}
			cout<<"Case #"<<in<<": "<<n*(i-1)<<endl;;
			}
			in++;
			
		}
		
	return 0;
}
