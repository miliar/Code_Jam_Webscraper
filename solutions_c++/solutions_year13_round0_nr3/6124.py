#include<cstdio>
#include<string>
#include<fstream>
using namespace std;

int n,a,b,p;

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	fin>>n;
	for(int i=1;i<=n;i++)
	{
		p=0;
		if(i!=1)fout<<endl;
		fin>>a>>b;
		if(a<=1&&b>=1)p++;
		if(a<=4&&b>=4)p++;
		if(a<=9&&b>=9)p++;
		if(a<=121&&b>=121)p++;
		if(a<=484&&b>=484)p++;
		fout<<"Case #"<<i<<": "<<p;
	}
	return 0;
}