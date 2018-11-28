#include<fstream.h>
#include<conio.h>
#include<stdlib.h>
#include<math.h>
void main()
{
clrscr();
ifstream d("input1.txt");
char test[100];
d>>test;
int z=atoi(test);
for(int i=1;i<=z;i++)
	{
	d>>test;
	float C=atof(test);
	d>>test;
	float B=atof(test);
	d>>test;
	float X=atof(test);

	double ctime=0;
	int n=0,t=0;
	do
		{
		double u=C/(n*B+2),r=X/(n*B+2);
		if((ctime+u+(X/(n*B+2+B)))<(ctime+r))
			 {
			 ctime+=u;n++;
			 }
		else    {
			ctime+=r;t++;
			}
		}
		while(t==0);
		ofstream po("output.txt",ios::app);
	  po<<ctime;
		if(ctime==abs(ctime))
			po<<".0000000"<<endl;
		else
			po<<"0000000"<<endl;

		po.close();

	}

  d.close();
}