#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main()
{
	clrscr();
	double c,rate,x,f;
	int cases;
	ifstream fin;
	ofstream fout;
	fin.open("A1.in",ios::in);
	fin>>cases;
	fout.open("AB.txt",ios::out);
	double tc=0;
	rate=2;
	int i=0;
	while(cases>0)
	{
		fin>>c>>f>>x;   tc=0;  rate=2;
		i++;

	for(;;)
	{
		double t1=tc+x/rate;
		tc+=c/rate;
		rate+=f;
		double t2=tc+x/rate;
		if(t1<t2)
		{
			fout<<"Case #"<<i<<": "<<t1<<endl;
			break;
		}
	}
		cases--;
	}
getch();
}





















