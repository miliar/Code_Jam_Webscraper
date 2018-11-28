#include<iostream>
#include<cmath>
#include<cstdio>
#include<string>
using namespace std;

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("output.txt","w+",stdout);
	int cases;
	cin>>cases;
	cout << "Case #1:\n";
	long long int n,jamcoins,count=0;
	cin>>n>>jamcoins;
	long long int bin_num=pow(2,n-1)+1;
	while(bin_num<=pow(2,n)-1&&count<jamcoins)
	{
		long long int s[n];
		long long int temp=bin_num,outer_flag=0;
		long long int i=0;
		while(temp>=1)
		{
			s[i++]=temp%2;
			temp=temp/2;
		}
		long long int base=2,base_div[9];
		while(base<=10)
		{
			long long int num=0,i=0,flag=0;
			while(i<=n-1)
			{
				long long int power=1;
				for(int k=0;k<i;k++)
					power=power*base;
				num=num+(s[i]*power);
				i++;
			}
			//arry[base-2]=num;
			for(long long int j=2;j<=sqrt(num);j++)
			{
				if(num%j==0)
				{
					base_div[base-2]=j;
					flag=1;
					break;
				}
			}
			if(flag==0)       //flag=0 represents num is prime
			{
				outer_flag=1;
				break;
			}
			base++;
		}


		if(outer_flag==0)      //outer_flag=0 means we have to display the current bin_num
		{
			for(int i=0;i<n;i++)
				cout << s[n-i-1];
			cout << " ";

			for(long long int i=0;i<9;i++)
				cout << base_div[i] << " ";
			cout << "\n";
			count++;
		}
		bin_num+=2;
	}

	return 0;
}
