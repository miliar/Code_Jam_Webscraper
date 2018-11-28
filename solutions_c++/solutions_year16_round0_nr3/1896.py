#include <bits/stdc++.h>
using namespace std;
int c[40];
int num[10];
int n;
bool isprime(int x)
{
	if (x==2 || x==3 || x==5 || x==7) return true;
	for (int i=2;i*i<=x;i++)
		if (x%i==0)
			return false;
	return true;
}
int f(int x)
{
	for (int i=2;i<(1<<(n/2+1));i++)
	{
		if (isprime(i)==false) continue;
		int res=0;
		for (int j=0;j<n;j++)
		{
			res=(res*x+c[j])%i;
		}
		if (res==0)
			return i;
	}
	return -1;
}
void addone()
{
	int res=1;
	for (int i=n-2;i>=0;i--)
	{
		if (res==0) break;
		c[i]+=res;
		res=c[i]/2;
		c[i]%=2;
	}
}
void print()
{
	for (int i=0;i<n;i++)
		cout<<c[i];
	cout<<endl;
}
int main()
{
	int t,j;
	cin>>t;
	for (int cas=1;cas<=t;cas++)
	{
		cin>>n>>j;
		memset(c,0,sizeof(c));
		c[0]=c[n-1]=1;
		int cnt=0;
		while (cnt<j)
		{
			int count=0;
			for (int i=2;i<11;i++)
			{
				int temp=f(i);
				if (temp==-1)
					break;
				else
					num[count++]=temp;
			}
			if (count==9)
			{
				cnt++;
				for (int i=0;i<n;i++)
					cout<<c[i];
				cout<<" ";
				for (int i=0;i<8;i++)
					cout<<num[i]<<" ";
				cout<<num[8]<<endl;
			}
			addone();
			//print();
		}
	}

	return 0;
}