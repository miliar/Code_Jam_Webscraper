#include <fstream>
#include <cmath>
#define Bits 14
using namespace std;
ifstream fin("in.in");
ofstream fout("out3.out");
int test(long long k,long long a,long long b)
{
	long long temp=k;
	if(k<a || k>b) return 0;
	int arr[Bits];
	int len=0;
	while(k>0)
	{
		arr[len]=k%10;
		len++;
		k=k/10;
	}
	for(int i=0;i<len/2;i++)
	{
		if(arr[i]!=arr[len-i-1]) return 0;
	}
	//fout << temp << endl;
	return 1;
}
long long work(long long a,long long b,long long sum,int len)
{
	long long result=0;
	int temp=sqrt(b);
	temp=log(temp)/log(10);
	int mlen=temp+1;
	if(len>mlen/2)
	{
		long long sum1=sum;
		for(int i=0;i<=9;i++)
		{
			sum1=sum*10+i;
			long long sum2=sum;
			while(sum2)
			{
				sum1=sum1*10+sum2%10;
				sum2/=10;
			}
			result+=test(sum1*sum1,a,b);
		}
		sum1=sum;
		long long sum2=sum;
		while(sum2)
		{
			sum1=sum1*10+sum2%10;
			sum2/=10;
		}
		result+=test(sum1*sum1,a,b);
	}
	else
	{
		for(int i=0;i<=9;i++)
		{
			result+=work(a,b,sum*10+i,len+1);
		}
	}
	return result;
}
int main()
{
	
	int T;
	fin >> T;
	for(int i=0;i<T;i++)
	{
		long long a,b;
		fin >> a >> b;
		long long sum=0;
		fout << "Case #" << i+1 << ": " << work(a,b,0,1) << endl;
	}
	fin.close();
	fout.close();
	return 0;
}