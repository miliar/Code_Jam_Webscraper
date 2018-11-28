#include <iostream>
#include <cstdio>
using namespace std;

long long rev(long long number)
{
    long long revers=0;
    for( ; number!= 0 ; )
   {
      revers = revers * 10;
      revers = revers + number%10;
      number = number/10;
   }

   return revers;
}
long long mi(long long x,long long y)
{
    if(x>y)
        return y;
    else
        return x;
}

int main() {
	// your code goes here
	//freopen("input.in","r",stdin);
	//freopen("output.in","w",stdout);
    long long a[1000003];
    long long j;
    for(j=1;j<=1000000;j++)
    {
    	a[j]=-1;
    }
    long long y;
    a[1]=1;
    for(j=1;j<=1000000;j++)
    {
        if(a[j+1]==-1)
            a[j+1]=a[j]+1;
        else
        {
            a[j+1]=mi(a[j+1],a[j]+1);
        }
        y=rev(j);
        if(y<=1000000)
        {
            if(a[y]==-1)
            a[y]=a[j]+1;
        }


    }
	long long test;
	long long result;
	cin>>test;
	long long cas;
	for(cas=1;cas<=test;cas++)
	{
	    long long n;
        cin>>n;
		cout<<"Case #"<<cas<<": "<<a[n]<<endl;
	}
	return 0;
}
