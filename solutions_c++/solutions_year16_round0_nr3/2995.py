#include <bits/stdc++.h>
using namespace std;
long long convert(long long n,long long base)
{	long long ans=0;
	while(n>0)
	{ans=(ans*10)+(n%base);
		n=n/base;}
	return ans;	
}
long long checkprime(long long n,long long initial=2)
{	long long i=initial;
	while(i*i<=n)
	{if(n%i==0)	{return i;}
		i++;}
	return 0;
}
long long interpret(long long n,long long base)
{
	long long ans=0;
	for(int i=0;n>0;i++)
	{
		ans+=(n%10)*pow(base,i);
		n=n/10;
	}
	return ans;
}
int main()
{
	cout.tie(0);
    std::ios::sync_with_stdio(false);
    ifstream fin;
    fin.open("input.in",ios::in);
    ofstream fout;
    fout.open("output.txt",ios::out);
	int t,T;fin>>T;
	for(t=1;t<=T;t++)
	{
		fout<<"Case #"<<t<<": "<<endl;
		int n,j;
		fin>>n>>j;
		long long count=1,i,k,l=pow(2,n-1)+1,u=pow(2,n)-1, div[9]={0};
		for(i=l;(i<=u && count<=j);i+=2)
		{   
			long long str=convert(i,2);
			long long primeflag=0;
			for(k=0;k<=8;k++)
			{
				long long intprt=interpret(str,k+2);
				long long check=checkprime(intprt);
				if(check==0){primeflag=1;break;}
				else div[k]=check;
			}
			if(primeflag==1) {continue;}
			else{fout<<str<<" ";
			for(k=0;k<=8;k++)
				fout<<div[k]<<" ";
			fout<<endl;
			count++;}
		}		
	}
	return 0;
}