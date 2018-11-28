#include<bits/stdc++.h>
#define cin fin
#define cout fout
using namespace std;
const int N=1e5+5;

int a[N];
int n,J;

long long int b[N];
ifstream fin;
ofstream fout;

inline long long int pr(long long int p)
{
	for(long long int i=2;i*i<=p;i++)
		if(p%i==0)
			return i;
	return -1;
}

inline void f()
{
	if(!J)
		return;
	for(int i=2;i<=10;i++)
	{
		long long int z=0;
		long long int p=1;
		for(int j=n;j>=1;j--)
		{
			z+=p*a[j];
			p*=i;
		}
		b[i]=pr(z);
		if(b[i]==-1)
			return;
	}
	J--;
	for(int i=1;i<=n;i++)
		cout<<a[i];
	cout<<" ";
	for(int i=2;i<=10;i++)
		cout<<b[i]<<" ";
	cout<<endl;
}

void ch(int i)
{
	if(i==n)
	{
		f();
		return;
	}
	a[i]=0;
	ch(i+1);
	a[i]=1;
	ch(i+1);
}

int main()
{
	fin.open("11.in",ios::in);
	fout.open("11.out",ios::out);
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<":\n";
		cin >> n >> J;
		a[1]=a[n]=1;
		ch(2);
	}
	return 0;
}


