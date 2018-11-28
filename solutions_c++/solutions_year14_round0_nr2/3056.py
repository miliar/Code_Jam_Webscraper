#include<iostream>
#include<fstream>
#include<iomanip>
#include<math.h>
using namespace std;

int main()
{
ifstream  in("B-large.in");
ofstream out;
out.open("B-small-attempt0.txt",ios::trunc);
int n;
in>>n;
for (int i=0;i<n;i++)
	{
	float c,f,x;
	in>>c>>f>>x;
	double time;
	double m;
	m=1000000.000000000;
	int number=floor(x/c);
	if (number==0) m=x/2;
	else
	for (int i=0;i<=number;i++)
		{
		time=0.000000000;
		for (int j=0;j<i;j++)
			{
			//if ((c/(2+j*f)+x/(2+f*(j+1)))<x/(2+j*f))
			time=double(time+double(c/(2.0+j*f)));
		
			}
		time=double(time+double(x/(2.0+f*i)));
		if (m>time)  m=time;
		}
	out <<"Case #"<<i+1<<": "<<setprecision(7) << setiosflags(ios::fixed | ios::showpoint)<< m<< endl;
	}
return 0;
}
