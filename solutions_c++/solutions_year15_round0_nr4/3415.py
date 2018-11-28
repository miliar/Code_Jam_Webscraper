#include<iostream>
#include<fstream> 
using namespace std;

int run(int x,int r,int c)
{
	if (x==1) return 0;
	if (x==2)
	{
		if ( r*c % 2 == 0 ) return 0;
		else return 1;
	}
	if (x==3)
	{
		if (r*c == 6 || r*c == 9 || r*c == 12) return 0;
		else return 1;
	}
	if (x==4)
	{
		if (r*c == 12 || r*c == 16) return 0;
		else return 1;
	}
}

int main()
{
	ifstream f;
	ofstream f1;
	f.open("E:\\learn for fun\\code jam\\2015\\QD\\D-small-attempt1.in");
	f1.open("E:\\learn for fun\\code jam\\2015\\QD\\1.out");
	int t,i,j,max,result,x,r,c;
	char number[1111];
	int sum[1111];
	f>>t;
	for (i=0;i<t;i++)
	{
		f>>x>>r>>c;
		result = run(x,r,c);
		if (result == 0) f1<<"Case #"<<i+1<<": GABRIEL"<<endl;
		else f1<<"Case #"<<i+1<<": RICHARD"<<endl;
	}
	return 0;
}
