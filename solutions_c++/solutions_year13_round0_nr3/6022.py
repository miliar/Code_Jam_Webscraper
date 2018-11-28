#include<iostream>
#include<math.h>
#include<stdio.h>
#include<cmath>


using namespace std;

int issquare(int a);
int ispln(int b);
int main()
{
	int n,cnt[n];
	cin>>n;
	for(int i=0;i<n;i++)
	{
		int a,b;
		cin>>a;
		cin>>b;
		for(int j=a;j<=b;j++)
		{
			int k1=1;
			
			if((k1==issquare(j)) && (k1==ispln(j)))
				cnt[i]++;
		}
	}

	for(int i=0;i<n;i++)
	{
	cout<<"Case #"<<i+1<<": ";
	cout<<cnt[i]<<endl;
	
	}




	return 0;
}

int ispln(int num)
{
int n,digit, rev = 0;
     n = num;
     do
     {
         digit = num%10;
         rev = (rev*10) + digit;
         num = num/10;
     }while (num!=0);
     
     if(n == rev)
       return 1;

	else return 0;



}

int issquare(int n)
{
double d = (double)n;
int i=1;
if (n < 0)
        return 0;
    int root=(int)(sqrt(d));
   if((n == root * root) && (i==ispln(root)))
	return 1;
	else 
	return 0;



}














