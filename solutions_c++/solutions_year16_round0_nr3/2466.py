#include"header.h"

int main()
{
	int t,n,j,digit,num[32];
	long long int flag,bin,binaryGen,proof[9]={0};
	cin>>t>>n>>j;
	cout<<"Case #1: \n";
	binaryGen = pow(2,n-1)+1;
	while(j>0)
	{
		bin = binaryGen;
		int i=n-1;
		while(bin>0)
		{
			digit = bin%2;
			bin /= 2;
			num[i]=digit;
			i--;
		}
		for(int k=2;k<=10;k++)	
		{
			bin=0;
			for(i=0;i<n;i++)
			{
				bin+=num[i]*pow(k,n-1-i);
			}
			flag=isprime(bin);
			if(flag!=0)
			{
				proof[k-2]=flag;
			}
			else
			{
				break;
			}
			if(k==10)
			{
				for(i=0;i<n;i++)
				{
					cout<<num[i];
				}
				for(i=0;i<9;i++)
				{
					cout<<' '<<proof[i];
				}
				cout<<endl;
				j--;
			}
		}
		binaryGen+=2;
	}
	return 0;
}