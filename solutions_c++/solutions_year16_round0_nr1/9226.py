#include <iostream>
#include <cstring>
#define SIZE 10
using namespace std;

int canSleep(int * arr,int len)
{
	len=len-1;
	while(len>=0)
		{	
			if(arr[len]!=1)
				return 0;
			len=len-1;
		}
		return 1;
}
int main() {
	
	int arr[SIZE];
	long int t,i,n;
	memset(arr,0,sizeof(arr));
	cin>>t;
	for(i=1;i<=t;i++)
	{	
		 cin>>n;
		// cout<<"n:"<<n<<endl;
		 
		 long int temp,ans;
		 long int num=1;
		 if(n==0)
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		 else
		 { 	
			while(canSleep(arr,SIZE)==0)
			{
				temp=num*n;
				ans=temp;
				//cout<<"temp:"<<temp<<","<<ans<<endl;
				while(temp!=0)
				 {
				 	if(arr[temp%10]!=1);
				 				arr[temp%10]=1;
				 	temp=temp/10;
			 	 }
			 	num=num+1;
			}
			cout<<"Case #"<<i<<": "<<ans<<endl;
		 }
		 memset(arr,0,sizeof(arr));
	}
	return 0;
}