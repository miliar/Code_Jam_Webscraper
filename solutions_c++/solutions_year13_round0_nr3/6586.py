#include<iostream>
#include<cmath>

using namespace std;

int palindrome(int a)
{
	int temp= a,reverse=0;
 	while( temp != 0 )
   	{
      		reverse = reverse * 10;
      		reverse = reverse + temp%10;
      		temp = temp/10;
   	}
 
   	if ( a == reverse )
      		return 1;
   	else
      		return 0;
 
}

int main()
{
	int n,i,arr[10000];
	cin>>n;
	i=1;
	int count;
	while(i<=n)
	{
		int a=0,b=0,as=0,bs=0,k=0,res1=0,res2=0,l=0;
		count=0;
		cin>>a>>b;
		as=sqrt(a);
		bs=sqrt(b);
		while((as*as)<a)
		{
			as=as+1;
		}
		k=as;
		//cout<<as<<" "<<bs;
		while(k<=bs)
		{
			l=k*k;
			res1=palindrome(l);
			res2=palindrome(k);
			if(res1==1 && res2==1)
			{
				count=count+1;
				//cout<<l<<"\t";
			}
			k=k+1;			
		}
		arr[i]=count;
		i=i+1;
	}
	for(int j=1;j<=n;j++)
		cout<<"Case #"<<j<<": "<<arr[j]<<"\n";
	return 0;	
}


