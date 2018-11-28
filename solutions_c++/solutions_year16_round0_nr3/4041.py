#include<iostream>
#include<math.h>
using namespace std;
long long prime(long long a)
{
	long long i,flag=0;
	if(a%2==0)
	return 2;
	if(a%3==0)
	return 3;
	for(i=5;i*i<=a;i++)
	{
		if(a%i==0)
		{
			flag=1;
			break;
		}
	}
	if(flag==1)
	{
		return i;
	}
	else
	return 0;
}
long long  base(long long int a,long long int b)
{
	long long bi[17],k=0,t=0;
	long long sum=0;
	while(a>0)
	{
		bi[k]=(a%10)*pow(b,k);
		k++;
		a=a/10;
	}
	k--;
	while(k>=0)
	{
		sum=sum+bi[k];
		k--;
	}
	return sum;
	
}
long long int bas(long long a,int b)
{
	long long bi[17],k=0,t=0;
	long long sum=0;
	while(a>0)
	{
		bi[k]=(a%2)*pow(10,k);
		k++;
		a=a/2;
	}
	k--;
	while(k>=0)
	{

		sum=sum+bi[k];
		k--;
	}
	return sum;
}
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("output.txt","w+",stdout);
long long int a=32769,k;
int count=1,n,t,c;
cin>>t>>n>>c;
cout<<"Case #1:"<<endl;
while(count<=c)
{
long long 	int ans[11],ans1[11];
	long long int binary=bas(a,2);
	for(k=2;k<=10;k++)
	{
		ans[k]=base(binary,k);
	}
	k=2;
	while(k<=10)
	{
		ans1[k]=prime(ans[k]);
		if(ans1[k]==0)
		break;
		k++;
	}
	if(k==11)
	{
		cout<<binary<<" ";
		for(int p=2;p<=10;p++)
		cout<<ans1[p]<<" ";
		cout<<endl;
		a=a+2;
		count++;
	}
	else
	a=a+2;	
}
}
