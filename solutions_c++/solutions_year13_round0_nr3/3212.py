#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int d[20];

bool check(long long x)
{
	int k=0;
	long long xx=x;
	while (xx>0)
	{
		d[k]=xx % 10;
		k++;
		xx/=10;
	}
	bool tf=true;
	for (int i=0;i<k;i++)
		if (d[i]!=d[k-1-i]) tf=false;
	return(tf);
}

int main()
{
	string ipath="C-small-attempt0.in",opath="1.out";
	ifstream infile(ipath,ios::in);
	ofstream outfile(opath,ios::out);
	int n,t;
	long long a,b;
	int ans;
	infile>>t;
	for (int loop=1;loop<=t;loop++)
	{
		infile>>a>>b;
		ans=0;
		outfile<<"Case #"<<loop<<": ";
		for (int i=int(sqrt(a));i<=int(sqrt(b));i++)
			if ((i*i>=a)&&(i*i<=b))
				if (check(i)&&check(i*i))
					ans++;
		outfile<<ans<<"\n";
	}
}