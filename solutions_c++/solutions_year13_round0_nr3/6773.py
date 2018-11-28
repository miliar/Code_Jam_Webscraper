#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	int n,a,b,i,j,k,temp,rev,rev1;
	cin>>n;
	
	if((n<1)||(n>100))
	{
		cout<<"\nIllegal Value of test cases";
		return 0;
	}
	int arr[100];
	for(i=0;i<n;i++)
	{
		cin>>a>>b;

		if((a<1)||(b<1)||(a>1000)||(b>1000)||(a>b))
		{
			cout<<"\nIllegal Value of data";
			return 0;
		}
		
		//a=sqrt(a);
		//b=sqrt(b);
		arr[i]=0;
		for(j=a;j<=b;j++)
		{
			k=sqrt(j);
			if(k*k!=j)
				continue;		
			temp=k;
			rev=0;
			while(temp!=0)
			{
				rev=rev*10+(temp%10);
				temp/=10;
			}

			rev1=0;
			temp=j;
			while(temp!=0)
			{
				rev1=rev1*10+(temp%10);
				temp/=10;
			}

			if((rev==k)&&(rev1==j))
			{
				arr[i]++;
			}
		}
	}
	
	for(i=0;i<n;i++)
	{
		cout<<"Case #"<<(i+1)<<": "<<arr[i]<<"\n";
	}
	return 0;
}
