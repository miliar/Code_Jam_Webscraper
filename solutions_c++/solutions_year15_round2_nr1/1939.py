#include <iostream>
#include<stdio.h>
using namespace std;
int arr[1000005];
int rev(int number)
{
	int reverse=0;
	while(number!=0)
   {
      reverse = reverse * 10;
      reverse = reverse + number%10;
      number = number/10;
   }
   return reverse;
	}


int dhruv(int n,int c)
{
	c=c+1;
	if(n==1)
	return c;
	int x=rev(n);
	if(x<n&&n%10!=0)
	{
		return min(arr[x]+c, arr[n-1]+c);
	}
	return arr[n-1]+c;
	}


int main() {
	int t, n;
	
	arr[1]=1;
	for(int i=2; i<=1000001; i++)
	arr[i]=dhruv(i, 0);
	cin>>t;
	for(int i=1; i<=t; i++)
	{
		cin>>n;
		//cout<<arr[n]<<endl;
		printf("Case #%d: %d\n",i,arr[n]);
	}
	return 0;
}#include <iostream>
#include<stdio.h>
using namespace std;
int arr[1000005];
int rev(int number)
{
	int reverse=0;
	while(number!=0)
   {
      reverse = reverse * 10;
      reverse = reverse + number%10;
      number = number/10;
   }
   return reverse;
	}


int dhruv(int n,int c)
{
	c=c+1;
	if(n==1)
	return c;
	int x=rev(n);
	if(x<n&&n%10!=0)
	{
		return min(arr[x]+c, arr[n-1]+c);
	}
	return arr[n-1]+c;
	}


int main() {
	int t, n;
	
	arr[1]=1;
	for(int i=2; i<=1000001; i++)
	arr[i]=dhruv(i, 0);
	cin>>t;
	for(int i=1; i<=t; i++)
	{
		cin>>n;
		//cout<<arr[n]<<endl;
		printf("Case #%d: %d\n",i,arr[n]);
	}
	return 0;
}#include <iostream>
#include<stdio.h>
using namespace std;
int arr[1000005];
int rev(int number)
{
	int reverse=0;
	while(number!=0)
   {
      reverse = reverse * 10;
      reverse = reverse + number%10;
      number = number/10;
   }
   return reverse;
	}


int dhruv(int n,int c)
{
	c=c+1;
	if(n==1)
	return c;
	int x=rev(n);
	if(x<n&&n%10!=0)
	{
		return min(arr[x]+c, arr[n-1]+c);
	}
	return arr[n-1]+c;
	}


int main() {
	int t, n;
	
	arr[1]=1;
	for(int i=2; i<=1000001; i++)
	arr[i]=dhruv(i, 0);
	cin>>t;
	for(int i=1; i<=t; i++)
	{
		cin>>n;
		//cout<<arr[n]<<endl;
		printf("Case #%d: %d\n",i,arr[n]);
	}
	return 0;
}
