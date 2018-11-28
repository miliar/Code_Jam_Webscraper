#include<conio.h>
#include<iostream>
#include<cmath>
#include<fstream>
using namespace std;

ifstream in("text.txt");
ofstream out("result.txt");

class Case
{
	int A,B,flag;
public:
	void getData()
	{
		flag=0;
		in>>A;
		in>>B;
	}
	void check()
	{
		int temp;
		int tempi;
		float ftemp;
		for (int i = A; i <= B; i++)
		{
			ftemp = sqrtf(i);
			temp = ftemp;
			if(temp==ftemp)
			{
				int n=temp;
				int x=0,y=0;
				while(n>0)
				{
					x = (10*x) +(n%10);
					n=n/10;		
				}
				tempi=i;
				while(tempi>0)
				{
					y = (10*y) +(tempi%10);
					tempi=tempi/10;		
				}
				if((temp==x)&&(y==i))
				{
					flag++;
				}
			}
		}
	}

	void show()
	{
		out<<flag;
	}

};
int main()
{
	static int T = 100;
	Case caseArr[100];
	int noc;
	in>>noc;
	int i;
	for (i = 0; i < noc;i++)
	{
		caseArr[i].getData();
	}
	for ( i = 0; i < noc; i++)
	{
		caseArr[i].check();
	}
	for ( i = 0; i < noc; i++)
		{
			out<<endl<<"Case #"<<i+1<<":\t";
			caseArr[i].show();
		}
	
	_getch();
return 0;
}