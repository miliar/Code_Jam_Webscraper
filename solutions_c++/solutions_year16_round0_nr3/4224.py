#include<iostream>
#include<cmath>

using namespace std;

unsigned long long del[11];

bool prost(unsigned long long S,int i)
{
	unsigned long long j;
	for (j=2; j<=sqrt(S+0.); j++)
	{
		if (S%j==0)
		{
			del[i]=j;
			return false;
		}
	}
	return true;
}

bool yes(unsigned long long M[],unsigned long long N,unsigned long long i)   // i - основание
{
	unsigned long long S=0,P=1,j;
	for (j=0; j<N; j++)
	{
		S+=M[N-1-j]*P;
		P*=i;
	}
	return (!prost(S,i));    // вернет false, если число простое
}		

bool podkh(unsigned long long M[],unsigned long long N)
{
	for (int i=2; i<=10; i++)
	{
		if (!yes(M,N,i))         // число не подходит, если оно простое
		{
			return false;
		}
	}
	return true;
}

void f(unsigned long long z,unsigned long long N,unsigned long long M[])
{
	int j=N-2;
	for (int i=1; i<=N-2; i++)
	{
		M[i]=0;
	}
	while (z!=0)
	{
		M[j]=z%2;
		z=int(z/2);
		j--;
	}
}

int main()
{
	freopen("input_file_name.in.txt","r",stdin);
	freopen("output_file_name.out","w",stdout);
	unsigned long long M[32],J,N,T,i,kol,X=1,z;
	cin>>T;
	for (i=1; i<=T; i++)
	{
		cin>>N>>J;
		kol=0;
		cout<<"Case #"<<i<<":"<<endl;
		M[0]=1;
		M[N-1]=1;
		for (z=1; z<=N-2; z++)          // X в степени N-2
		{
			X*=2;
		}
		for (z=0; z<=X && kol!=J; z++)
		{
			f(z,N,M);
			if (podkh(M,N))
			{
				for (int q=0; q<N; q++)
				{
					cout<<M[q];
				}
				cout<<" ";
				for (int q=2; q<=10; q++)
				{
					cout<<del[q]<<" ";
				}
				cout<<endl;
				kol++;
			}
		}
	}
	return 0;
}