#include<bits/stdc++.h>
#define cin fin
#define cout fout
using namespace std;
const int N=1e5+5;

bool mark[20];

inline long long int f(long long int x)
{
	memset(mark,0,sizeof(mark));
	int t=0;
	for(int i=1;i<=2000000;i++)
	{
		long long int p=x*i;
		while(p)
		{
			if(!mark[p%10])
			{
				t++;
				mark[p%10]=1;
			}
			p/=10;
		}
		if(t==10)
			return x*i;
	}
	return -1;
}

int main()
{
	ifstream fin;
	fin.open("11.in",ios::in);
	ofstream fout;
	fout.open("11.out",ios::out);
	int t;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		int n;
		cin >> n;
		int x=f(n);
		cout<<"Case #"<<i<<": ";
		if(x==-1)
			cout<<"INSOMNIA";
		else
			cout<<x;
		cout<<endl;
	}
	return 0;
}


