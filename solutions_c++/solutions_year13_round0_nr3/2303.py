#include <fstream>
using namespace std;

//10^n;
long long tp(int n)
{
	if(n==0) return 1;
	else return 10*tp(n-1);
}
bool isHui(long long n)
{
	//��಻��16λ��
	long long y[18];
	int front;
	for(int i=17;i>=0;i--)
	{
		y[i]=(n%tp(i+1))/tp(i);
	}
	for(front=17;front>=0;front--)
	{
		if(y[front]!=0) break;
	}
	//front�ǵ�һ����Ϊ�������
	for(int i=0;i<=front/2;i++)
	{
		if(y[i]!=y[front-i])
			return false;
	}
	return true;
}
int main()
{
	ifstream fin("C-large-1.in");
	ofstream fout("C-large-1.out");
	/*ifstream fin("B-large.in");
	ofstream fout("B-large.out");*/
	long long result[1000];
	int num=0;

	//�Լ��������������Ϊ9999999^2�����һ��������14λ������
	//1λ��
	for(long long i=1;i<=9;i++)
	{
		if(isHui(i*i)) result[num++]=i*i;
	}
	//2λ
	for(long long i=1;i<=9;i++)
	{
		long long k=i*10+i;
		if(isHui(k*k)) result[num++]=k*k;
	}
	//3λ
	for(long long i=1;i<=9;i++)
	{
		for(long long j=0;j<=9;j++)
		{
			long long k=i*100+j*10+i;
			if(isHui(k*k)) result[num++]=k*k;
		}
	}
	//4λ
	for(long long i=1;i<=9;i++)
	{
		for(long long j=0;j<=9;j++)
		{
			long long k=i*1000+j*100+j*10+i;
			if(isHui(k*k)) result[num++]=k*k;
		}
	}
	//5λ
	for(long long i=1;i<=9;i++)
	{
		for(long long j=0;j<=9;j++)
		{
			for(long long x=0;x<=9;x++)
			{
				long long k=i*10000+j*1000+x*100+j*10+i;
				if(isHui(k*k)) result[num++]=k*k;
			}
		}
	}
	//6λ
	for(long long i=1;i<=9;i++)
	{
		for(long long j=0;j<=9;j++)
		{
			for(long long x=0;x<=9;x++)
			{
				long long k=i*100000+j*10000+x*1000+x*100+j*10+i;
				if(isHui(k*k)) result[num++]=k*k;
			}
		}
	}
	//7λ
	for(long long i=1;i<=9;i++)
	{
		for(long long j=0;j<=9;j++)
		{
			for(long long x=0;x<=9;x++)
			{
				for(long long y=0;y<9;y++)
				{
					long long k=i*1000000+j*100000+x*10000+y*1000+x*100+j*10+i;
					if(isHui(k*k)) result[num++]=k*k;
				}
			}
		}
	}
	//8λ
	for(long long i=1;i<=9;i++)
	{
		for(long long j=0;j<=9;j++)
		{
			for(long long x=0;x<=9;x++)
			{
				for(long long y=0;y<9;y++)
				{
					long long k=i*10000000+j*1000000+x*100000+y*10000+y*1000+x*100+j*10+i;
					if(isHui(k*k)) result[num++]=k*k;
				}
			}
		}
	}
	int T;
	long long A,B;
	int a=-1,b=-1;
	fin>>T;
	for(int t=1;t<=T;t++)
	{
		fin>>A>>B;
		a=-1;
		b=-1;
		for(int i=0;i<num;i++)
		{
			if(a==-1)
			{
				if(A<=result[i]) a=i;
			}
			if(b==-1)
			{
				if(B<result[i]) 
				{
					b=i;
					break;
				}
			}
		}
		fout<<"Case #"<<t<<": "<<b-a<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

