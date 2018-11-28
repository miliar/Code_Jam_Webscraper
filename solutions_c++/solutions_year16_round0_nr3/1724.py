#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

const long long N=16;
const long long J=50;


	
	
	long long SuShu(long long num)
	{
		long long n=(long long)(sqrt((double)num));
		for(long long i=2;i<=n;i++)
		{
			if(num%i==0)
				return i;
		}
		return 1;
	}
	
	long long Base(long long num,long long b)
	{
		long long sum=0;
		long long bb=1;
		while(num!=0)
		{
			//sum*=b;
			sum+=num%10*bb;
			bb*=b;
			num/=10;
		}
		return sum;
	}
	long long Two(long long num)
	{
		long long sum=0;
		long long bb=1;
		while(num)
		{
			
			sum+=(num&1)*bb;
			bb*=10;
			num=num>>1;
		}
		return sum;
	}

int main()
{
	long long n2[17];
	n2[0]=1;
	for(long long i=1;i<=N;i++)
	{
		n2[i]=2*n2[i-1];
	}
	long long count=0;
	ofstream fout("C.large");
	for(long long i=n2[N-1]-1;i<n2[N];i+=2)
	{
		long long i10=Two(i);
		long long res[10];
		bool flag=true;
		for(long long j=2;j<=10;j++)
		{
			if(j<10)
				res[j-1]=SuShu(Base(i10,j));
			else
				res[j-1]=SuShu(i10);
			if(res[j-1]==1)
			{
				flag=false;
				break;
			}
		}
		if(flag)
		{
			res[0]=i10;
			count++;
			fout<<res[0];
			for(long long j=1;j<10;j++)
				fout<<" "<<res[j];
			fout<<endl;
			if(count>J)
			{
				fout.close();
				return 0;
			}
		}

		


	}

	return 0;
}