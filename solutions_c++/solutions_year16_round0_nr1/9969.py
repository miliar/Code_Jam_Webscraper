#include <bits/stdc++.h>
using namespace std;
int num[10]={0};
int main()
{

	ifstream fin("A-large.in");
	ofstream fout("ou.txt");
	int t;
	long long n;
	fin>>t;
for (int j=1;j<=t;j++)
{
		fin>>n;
	int cnt=0;
	int ans=0;
	long long last=-1;
	for (long long i=n;cnt<=100000;cnt++,i+=n)
	{
		long long x=i;
		while (x)
		{
			int y=x%10;
			x/=10;
			if (num[y]==0) {ans++; num[y]=1;}
		}
		if (ans==10) {last=i; break;}
	}

	if (last==-1)
	fout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
	else 	fout<<"Case #"<<j<<": "<<last<<endl;
	memset(num,0,sizeof(num));

		}
}
