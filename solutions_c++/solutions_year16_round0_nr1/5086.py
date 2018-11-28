#include<iostream>

using namespace std;

bool M[10];

long long son(long long N)
{
	long long k=0,buf,p,j;
	for (j=0; j<=9; j++)
	{
		M[j]=false;
	}
	for (j=N; k!=10; j+=N)
	{
		buf=j;
		while (j!=0)
		{
			p=j%10;
			if (M[p]==false)
			{
				M[p]=true;
				k++;
			}
			j=(long long)(j/10);
		}
		j=buf;
	}
	j-=N;
	return j;
}

int main()
{
	long long N,T;
	cin>>T;
	for (int i=1; i<=T; i++)
	{
		cin>>N;
		cout<<"Case #"<<i<<": ";
		if (N==0)
		{
			cout<<"INSOMNIA"<<endl;
		}
		else
		{
			cout<<son(N)<<endl;
		}
	}
	return 0;
}