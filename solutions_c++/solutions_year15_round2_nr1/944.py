#include<math.h>
#include<iostream>
using namespace std;

long long fn(long long n)
{
	long long result=0;
	//cout<<"\n n= "<<n;
	if(n==1)
		return 1;
	else if(n==101)
		return 30;
	else if(n==1001)
		return 139;
	else if(n==10001)
		return 338;
	else if(n==100001)
		return 1437;
	else if(n==11)
		return 11;
	else if(n==1000001)//6
		return 3436;
	else if(n==10000001)//7
		return 14435;
	else if(n==100000001)//8
		return 34434;
	else if(n==1000000001)//9
		return 144433;
	else if(n==10000000001)
		return 344432;
	else if(n==100000000001)//11
		return 1444431;
	else if(n==1000000000001)//12
		return 3444430;
	else if(n==10000000000001)//13
		return 14444429;
	else if(n==100000000000001)//14
		return 34444428;
	int length=0;
	long long temp=n;
	long long rev=0;
	while(temp)
	{
	rev=10*rev+temp%10;
	temp/=10;
	length++;
	}
	long long t;
	if(length%2==0)
	{

		t=n%(long long)pow(10,length/2)-1;
	}
	else
	{
		t=n%(long long)pow(10,(length+1)/2)-1;
	}		
		if(t==-1)
		{
		result=1+fn(n-1);
		}
		else if(t==0)
		{
		result++;
		//cout<<"\n t= "<<t<<" calling fn here res= "<<result;
		result=result+fn(rev);
		}
		else
		{
		result=result+t;
					
		//cout<<"\n t= "<<t<<" calling fn here res= "<<result;
		result=result+fn(n-t);
		}	
	
		
	return result;
}

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
	long long n;
	cin>>n;
	cout<<"Case #"<<i<<": "<<fn(n)<<"\n";
//	cout<<"\nfinal res: "<<fn(n);
	}
}
