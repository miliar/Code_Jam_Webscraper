#include<fstream.h>
#include<math.h>
void main()
{
	int t,a,b,m,n,count,i=1;
	int pal(int);
	ifstream fin;
	ofstream fout;
	fin.open("abc.in",ios::in);
	fout.open("out.out",ios::out);
	fin>>t;
	while(t--)
	{
		fin>>a>>b;
		m=sqrt(a);
		n=sqrt(b);
		if(m*m!=a)
			m++;
		count=0;
		for(;m<=n;m++)
		{
			if(pal(m))
				if(pal(m*m))
					count++;
		}
		fout<<"Case #"<<i++<<": "<<count<<"\n";
	}
	fin.close();
	fout.close();
}
int pal(int n)
{
	int a=0,b;
	b=n;
	while(b>0)
	{
		a=a*10+b%10;
		b/=10;
	}
	if(a==n)
		return 1;
	return 0;
}