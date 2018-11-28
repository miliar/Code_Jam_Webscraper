#include<bits/stdc++.h>
using namespace std;
int main()
{	
	ifstream f1("A-large.in");
	ofstream f2("A-large_ans1.txt");
	int t;
	f1>>t;
	long long n;
	int x=1;
	while(t--)
	{
		f1>>n;
		int a[10]={0};
		long long k,j=n;
		f2<<"Case #"<<x++<<": ";
		if(n!=0)
		while(n)
		{	int check=0;
			k=n;
		for(int i=0;k!=0;i++)
		{	a[k%10]++;
			k/=10;
		}
		for(int i=0;i<10;i++)
			if(a[i]==0)
			{	n+=j;break;}
			else check++;
		if(check==10)
		{f2<<n<<'\n';n=0;break;}
		}
		else f2<<"INSOMNIA"<<'\n';
	}
	f1.close();
	f2.close();
	return 0;
}
