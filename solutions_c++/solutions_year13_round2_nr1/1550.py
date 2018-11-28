#include<iostream>
#include<algorithm>
#include<fstream>

using namespace std;
int a[105],n;

ifstream ifile("D:/in1.in");
ofstream ofile("D:/out.txt");

int f(int x,int r,int s)
{
	if(x==n) return 0;
	int u,c;
	for(u=s,c=0;u<=a[x];++c,u+=u-1);
	u+=a[x];
		cout<<a[x]<<" "<<c<<" "<<s<<endl;
	c+=f(x+1,r-1,u);

	if(c>r) return r;
	return c;
}

int main()
{
	int x,m,t,tc,s;
	ifile>>t;
	for(tc=0;tc<t;++tc)
	{
		ifile>>m>>n;
		for(x=0;x<n;++x)
		{
			ifile>>a[x];
		}
		sort(a,a+n);
		s=m;
		for(x=0;x<n;++x)
		{
			if(s<=a[x]) break;
			s+=a[x];
		}
		if(x==n) ofile<<"Case #"<<tc+1<<": "<<0<<endl;
		else
		{
			if(m==1) ofile<<"Case #"<<tc+1<<": "<<n<<endl;
			else
			{
				ofile<<"Case #"<<tc+1<<": "<<f(x,n-x,s)<<endl;
			}
		}
	}
	return 0;
}
			