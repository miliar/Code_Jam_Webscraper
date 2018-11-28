# include <iostream>
# include <cstdlib>
# include <cmath>
# include <fstream>
using namespace std;
int pal(int n,int l)
{
	if (n<10)
		return 1;
	else
	{
		char s[100];
		itoa(n,s,10);
		int v=l-1;
		for (int i=0;i!=v;i++,v--)
		{
			if (i==v || i>v)
				break;
			if (s[i]!=s[v])
			{
			return 0;
			}
		}
		return 1;
	}
}
char s[100]={0};
int main ()
{
	ofstream fout("small-c.txt");
int t;
cin>>t;
for (int counter=0;counter<t;counter++)
{
int begin,end,ans=0;;
cin>>begin>>end;
for (int i=begin;i<=end;i++)
{
	long double k=i;
	double d=sqrt(k);

	if (d==(int)d)
	{
		int u=0;
		int y=k;
		int j=d;
		int p=0;
		while (y!=0)
		{
		y=y/10;
		u++;
		if (j!=0)
			p++;
		j=j/10;
		}
		if (pal(d,p)==1 && pal(k,u)==1)
		{
			
			ans++;
		}
	}
	
}

fout<<"Case #"<<counter+1<<": "<<ans<<endl;


}
}