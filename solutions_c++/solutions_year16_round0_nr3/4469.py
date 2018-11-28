#include <bits/stdc++.h>
using namespace  std;
int long long temp[9];
long long int  co12(long long int N)
{   long long int k=0;long long int sum=0;long long int x;
      while(N!=0)
     { 
      x = N % 2;
     sum+=((long long int)pow(10,k))*x;
     k++;
   N /= 2;
   }
   return sum;
   
}
long long co(long long int N, int b)
{   long long int k=0,sum=0;
      while(N!=0)
     {
     int x = N %10;
     sum+=(long long int)pow(b,k)*x;
     k++;
   N /= 10;
   }
   return sum;
   
}

int isNotPrime(long long k,long long l)
{
	for(long long int i=2;i*i<=k;i++)
	{
		if(k%i==0){
		temp[l]=i;
		return 1;}
	}
	return 0;
}
int main()
{
	FILE *input,*output;
	input=fopen("input.txt","r");int t;
	output=fopen("output.txt","w");
	fscanf(input,"%d",&t);
	while(t--)
{long long int n3,n4; 
fscanf(input,"%lld %lld",&n3,&n4);
long long int c=0;
n3=co(n3,10);
fprintf(output,"Case #1:\n");
for(long long int n=32769;c!=50;n=n+2)
{ long long int n1;
if( isNotPrime(n,0)&& c!=50 )
{  
n1=co12(n);
	if(isNotPrime(co(n1,9),1))
	{ 
	if(isNotPrime(co(n1,8),2))
	{
	if(isNotPrime(co(n1,7),3))
	{
	if(isNotPrime(co(n1,6),4))
	{
	if(isNotPrime(co(n1,5),5))
		{
	if(isNotPrime(co(n1,4),6))
	{
	if(isNotPrime(co(n1,3),7))
	{
	if(isNotPrime(n1,8))
	{  fprintf(output,"%lld",n1);
for(int i=0;i<9;i++)fprintf(output," %lld",temp[i]);
	c++;fprintf(output,"\n");
	
	}
}
}
}
}
}
}
}
}

}
}
}
