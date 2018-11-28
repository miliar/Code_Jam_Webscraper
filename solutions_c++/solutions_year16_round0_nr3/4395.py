#include <iostream>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <cstring>
#include <vector>
using namespace std;
int t,len,n;
vector <string> kombinasi;
long long arr[10];
long long isprime(long long a)
{
	for(int i=2;i<=sqrt(a);i++)
	{
		if(a%i==0)
		{
			return i;
		}
	}
	return -1;
}
long long base(int a,string b)
{
	long long tambah=1,hasil=0;
	for(int i=b.length()-1;i>=0;i--)
	{
		if(b[i]=='1')
		{
			hasil+=tambah;
		}
		tambah*=a;
	}
	return hasil;
}
long long kombin(int a,string b)
{
	if(b.length()==a)
	{
		if(b[b.length()-1]=='1')
		kombinasi.push_back(b);
	}
	else
	{
		kombin(a,b+'0');
		kombin(a,b+'1');
	}
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	for(int i=1;i<=t;i++)	
	{
		int idx=0;
		scanf("%d%d",&len,&n);
		printf("Case #%d:\n",i);
		kombin(len,"1");
		while(n>0)
		//while(idx<kombinasi.size())
		{
			//cout<<kombinasi[idx]<<endl;
			for(int j=2;j<=10;j++)
			{
				arr[j]=isprime(base(j,kombinasi[idx]));
				if(arr[j]==-1)
				goto lanjut;
			}
			cout<<kombinasi[idx];
			for(int j=2;j<=10;j++)
			{
				printf(" %lld",arr[j]);
			}
			cout<<endl;
			n--;
			lanjut:
			idx++;
		}
		kombinasi.clear();
	}
}
