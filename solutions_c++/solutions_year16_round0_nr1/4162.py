#include <iostream>
using namespace std;

int main() {
	// your code goes here
	freopen("input1.txt","r",stdin);
	freopen("ans1.txt","w",stdout);
	long long int t,z;
	cin>>t;
	for(z=1;z<=t;z++)
	{
		long long int n,temp,j,sum,i;
		int a[10]={0};
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<z<<": INSOMNIA"<<endl;
		}
		else
		{
		
		for(i=1;;i++)
		{
			sum=0;
			temp=i*n;
			while(temp!=0)
			{
				a[temp%10]=1;
				temp=temp/10;
			}
			for(j=0;j<10;j++)
			{
				sum=sum+a[j];	
			}
			if(sum==10)
			{
				cout<<"Case #"<<z<<": "<<i*n<<endl;
				break;
			}
		}
		}
		
	}
	return 0;
}