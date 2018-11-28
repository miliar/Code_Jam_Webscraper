#include<iostream.h>
#include<iomanip.h>
#include<fstream.h>
#include<conio.h>

void main()
{
	int T,c=0;
	double C,F,X,ck=2,s=0,T1,T2;
	ifstream fin;
	ofstream fout;
	clrscr();

	fin.open("C1.in",ios::in);
	fout.open("C1.txt",ios::out);
	fin>>T;
	while(T--)
	{
		c++; ck=2.0; s=0;
		fin>>setprecision(7)>>C>>F>>X;

		for(;;)
		{
			T1=s+X/ck;
			s+=(C/ck);
			ck+=F;
			T2=s+X/ck;

			if(T1<T2)
			{
				cout<<"Case #"<<c<<": "<<setprecision(7)<<(float)T1<<endl;
				fout<<"Case #"<<c<<": "<<setprecision(7)<<(float)T1<<endl;
				break;
			}
		}
	}
	fin.close();
	fout.close();
	getch();
}
