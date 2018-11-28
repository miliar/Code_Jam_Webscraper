#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
#include<stdio.h>
#include<fstream.h>
#include<math.h>
void main()
{
	clrscr();
	int t,x=0;
	ifstream fin;
	ofstream fout;
	fout.open("001.txt",ios::out);
	fin.open("np.txt",ios::in);
	fin>>t;
	int fnum,snum;
	char b;
	while(t>0)
	{
		x++;
		int count=0;
			int flag=0;
			fin>>fnum;
			fin.get(b);
			fin>>snum;
			double a;
			a=log(snum)/log(2);
			if(snum%2!=0)
			{
				flag=123;
				goto ans;
			}
			else
			{
				int ctr=0;
				while(ctr<50)
				{
					ctr++;
					if(fnum>=snum)
					{
					goto ans;
					}
					count++;
					snum=snum/2;
					if(ctr==40)
					{
						flag=123;
						goto ans;
					}
				}
			}
				ans:

			if(flag==123)
				fout<<"Case #"<<x<<": impossible"<<endl;
			else if(a<count)
				fout<<"Case #"<<x<<": "<<a<<endl;
			else
				fout<<"Case #"<<x<<": "<<count<<endl;
		t--;
	}
getch();
}