#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;

int T=0;

class Revenge
{
private:
	int n;
	char a[105];
	int a2[105];
	void input();
public:
	void solve();
	int count;
};

void Revenge :: input()
{
	scanf("%s", a);
	n=strlen(a);
	for (int i=0; i<=n-1; i++)
	{
		if(a[i]=='+') a2[i]=1;
			else a2[i]=0;
	}
}

void Revenge :: solve()
{
	input();
	int k=0;
	if (a2[0]==0) k=1;
	for (int i=1; i<=n-1; i++)
	{
		if(a2[i]!=a2[i-1]&&a2[i]==0)
			k+=2;
	}
	cout<<"Case #"<<count<<": "<<k<<endl;
}

int main()
{
	freopen("bbb.in", "r", stdin);
	freopen("output2.out", "w", stdout);
	cin>>T;
	for(int i=1; i<=T; i++)
	{
		Revenge* a = new Revenge();
		a->count = i;
		a -> solve();
	}
	return 0;
} 
