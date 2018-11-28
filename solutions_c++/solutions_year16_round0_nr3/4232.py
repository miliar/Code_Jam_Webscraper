#include<stdio.h>
#include<iostream>
#include<string.h>
#include<iomanip>
#include<math.h>
using namespace std;
long long int decimal_binary(long long int n);
long long int basen(long long int num,int n);
long long int isPrime(long long int n);
int main()
{
	int cnt=0,t,n,var;
	long long int arr[50][10];
	scanf("%d",&t);
	scanf("%d %d",&n,&var);
	for(long long int k=0;k<pow(2,n-2);k++)
	{	
		if(cnt==var)
			break;
		long long int basei;
		int flag[9];
		for(int i=2;i<11;i++)
		{
			long long int basei;
			if(i!=2)
			{
				long long int binary=decimal_binary(k);
				//printf("%d,%lld\n",i,binary);
				basei=basen(binary,i);
				basei=basei*i;
			}
			else if(i==2)
				basei=k*2;
			basei=basei+pow(i,n-1)+1;
//			printf("%d,%lld\n",i,basei);
			//printf("%d,%lld\n",i,basei);	
			long long int ans=isPrime(basei);
			if(ans==-1)
			{
				flag[i-2]=-1;
				break;
			}
			else
			{
				flag[i-2]=ans;
			}
		}
		int temp=0;	
		for(int j=0;j<9;j++)
		{	
			if(flag[j]==-1)
			{
				temp=1;
				break;
			}
		}
		if(temp==0)
		{
			arr[cnt][0]=k;
			for(int j=0;j<9;j++)
			{
				arr[cnt][j+1]=flag[j];
			}
			cnt++;
		}
	}
	printf("Case #1:\n");
	for(int i=0;i<var;i++)
	{
		for(int j=0;j<10;j++)
		{
			
			if(j==0)
			{
				long long int ans=decimal_binary(arr[i][j]);
				cout<<"1"<< setfill('0')<<setw(n-2)<<ans<<"1 ";
			}
			else
				printf("%lld ",arr[i][j]);	
		}
		printf("\n");
	}			
	return 0;
}						
long long int isPrime(long long int n){
    long long int i;

    if (n==2)
        return -1;

    if (n%2==0)
        return 2;

    for (i=3;i<=sqrt(n);i+=2)
        if (n%i==0)
            return i;

    return -1;
}		
			
long long int basen(long long int num,int n) 
{
    long long int decimal=0, i=0, rem;
    while (num!=0)
    {
        rem = num%10;
        num/=10;
        decimal += rem*pow(n,i);
        ++i;
    }
    return decimal;
}


			
long long int decimal_binary(long long int n)  
{
    long long rem, i=1, binary=0;
    while (n!=0)
    {
        rem=n%2;
        n/=2;
        binary+=rem*i;
        i*=10;
    }
    return binary;
}
