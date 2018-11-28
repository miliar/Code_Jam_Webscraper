#include <iostream>
#include <algorithm>
#include <fstream>
#include <string.h>
#define lli long long int
using namespace std;
fstream fin,fout;
lli A[100000],B[100000];
lli gcd(lli a,lli b)
{
    int rem;
    if(b==0)
    return a;
    if(a==0)
    return b;
    if(b>a)
    {
           a=a+b;
           b=a-b;
           a=a-b;
    }
    rem=a%b;
    while(rem>0)
    {
        a=b;
        b=rem;
    	rem=a%b;
	}
	if(rem==0)
    return b;
    else
    return rem;
}                        
lli findmin(lli b)
{
	lli min=B[1],ind=1;
	for(lli i=2;i<=b;i++)
	{
		if(B[i]<min)
		{
			min=B[i];
			ind=i;
		}
	}
	return ind;
}
int main()
{
	fin.open("in.cpp");
	fout.open("output.cpp");
	//#define fin cin
	//#define fout cout
	lli t,n,I,b;
	fin>>t;
	for(I=1;I<=t;I++)
	{
		memset(B,0,sizeof(B));
		fout<<"Case #"<<I<<": ";
		fin>>b>>n;
		for(lli i=1;i<=b;i++)
		{
			fin>>A[i];
		}
		lli lcm;
		lcm=A[1]*A[2]/gcd(A[1],A[2]);
		
		for(lli i=3;i<=b;i++)
		{
			lcm=lcm*A[i]/gcd(lcm,A[i]);
		}
		//cout<<"lcm "<<lcm<<endl;
		lli sum=0;
		for(lli i=1;i<=b;i++)
		{
			sum+=lcm/A[i];
		}
		lli over=(n/sum-1)*sum;
		lli i,mn;
		for(i=1;i<=b;i++)
		{
			B[i]+=A[i];
			over++;
			if(over>=n)
			break;
		}
		while(over<n)
		{
			i=findmin(b);
			B[i]+=A[i];
			over++;
		}
		fout<<i<<endl;
	}
	
	fin.close();
	fout.close();
}
