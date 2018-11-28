#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>

using namespace std;
int a[40];
long long temp[20];
int n,c;

void fuck(long long tmp)
{
	memset(a,0,sizeof(a));
	a[1]=1;
	a[n]=1;
	int cnt=2;
	while(tmp)
	{
		a[cnt++]=tmp%2;
		tmp=tmp/2;
	}
}

long long prime(long long num)
{
	double s=sqrt((double)num)+0.5;
	for(long long i=2;i<=s;i++)
	{
		if(num%i==0)
			return i;
	}
	return 0;
}

int main()
{
	freopen("C-small-attempt4.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int ca=1;
	scanf("%d",&t);
	while(t--)
	{
		printf("Case #%d:\n",ca++);
		scanf("%d%d",&n,&c);
		int count=0;
		for(long long i=0;i<(1LL<<(n-1));i++)
		{
			fuck(i);
			bool f=true;
			int cnt=1;
			for(int k=2;k<=10;k++)
			{
				long long num=0;
				for(int j=n;j>=1;j--)
					num=num*k+a[j];
				long long tmp=prime(num);
				if(tmp==0)
				{
					f=false;
					break;
				}
				else
					temp[cnt++]=tmp;
			}
			if(f)
			{
				for(int j=n;j>=1;j--)
					cout<<a[j];
				for(int j=1;j<10;j++)
					cout<<" "<<temp[j];
				cout<<endl;
				count++;
			}
			if(count==c)
				break;
		}
	} 
 	return 0;
}


