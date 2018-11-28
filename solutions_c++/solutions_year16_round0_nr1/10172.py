#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int t,n;
bool f[10];

bool check()
{
	int i;
	for (i=0;i<=9;i++)
		if (!f[i])
			return false;
	
	return true;
}

void digit(int k)
{
	while (k)
	{
		f[k%10]=true;
		k/=10;
	}
	
	return ;
}

void cal(int o)
{
	int i,m;
	
	cin>>n;
	m=i=0;
	memset(f,false,sizeof(f));
	
	if (n==0)
	{
		cout<<"Case #"<<o<<": INSOMNIA\n";
		return ;
	}
	
	while (!check())
	{
		m+=n;
		i++;
		
		digit(m);
	}
	
	cout<<"Case #"<<o<<": "<<m<<endl;
	return ;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i;
	
	cin>>t;
	for (i=1;i<=t;i++)
		cal(i);
	
	
	return 0;
}
