#include <bits/stdc++.h>
#define lli long long int
using namespace std;
lli ans[1000009];
lli N = 1000002;

int solve(int n)
{
	int i,ctr;
	lli m,k;
	int alldigit[10];
	for(i=0;i<10;i++) alldigit[i]=0;

	m=n;
	while(m<N*1000 && m>=n)
	{
		k=m;
		while(k>0)
		{
			int r=k%10;
			k=k/10;
			alldigit[r]=1;	
		}
		int ctr=0;
		for(i=0;i<10;i++) ctr=ctr+alldigit[i];
		if(ctr==10) return m;
		m=m+n;
	}
	return -1;
}

int genans(int n)
{
	int i;
	ans[0]=-1;
	for(i=1;i<n;i++) ans[i]=solve(i);
}

int main()
{
	genans(N);

	fstream cinf;
	cinf.open ("A-large.in");

	fstream coutf;
	coutf.open ("Bsmall.txt");
	
	int t; cinf>>t;
	int k;
	for(int tt=1;tt<=t;tt++)
	{
		cinf>>k;
		if(ans[k]==-1)	coutf<<"Case #"<<tt<<": "<<"INSOMNIA"<<endl;
		else coutf<<"Case #"<<tt<<": "<<ans[k]<<endl;
	}

	cinf.close();
	coutf.close();
	//cout<<ans[558587]<<endl;
}
