#include<iostream>

using namespace std;
int check(long long int a, int*arr)
{
if(a==0)
{
	arr[0]=1;
}
else
while(a!=0)
{
	long long int temp=0;
	temp=a%10;
	arr[temp]=1;
	a=a/10;
}
int flag=1;
for(int i=0; i<10; i++)
if(arr[i]==0)
{
	flag=0;
	break;
}
return flag;
}
int main()
{
	
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w+",stdout);
	int t=0;
	cin>>t;
	long long int count=1;
	while(t--)
	{
		int arr[10];
		for(int i=0; i<10; i++)
		arr[i]=0;
		long long int n=0;
		
        
		cin>>n;
		long long int x=1;
		long long int temp=0;
		long long int sol=0;
		if(n!=0)
		{while(temp==0)
		{
			sol=x*n;
			x++;
            temp=check(sol,arr);			
 		}
 		cout<<"Case #"<<count++<<": "<<sol<<endl;}
 		else
 		cout<<"Case #"<<count++<<": INSOMNIA"<<endl;
		
	}
	return 0;
	
}
