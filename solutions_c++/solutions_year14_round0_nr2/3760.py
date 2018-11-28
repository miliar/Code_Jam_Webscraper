#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	int check,num;
	double time=0;
	double income=2;
	double answer;
	int i=1,j,k;
	int farms=0;
	int answer1,answer2;;
	double c,f,x;
	int dec=0;
	double last,current;
	int size,n;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin>>size;
	for(k=0;k<size;k++)
	{
		
		fin>>c;
		fin>>f;
		fin>>x;
		answer=x/2;
		farms=0;
		while(true)
		{
			last=0;
			current=0;
			for(i=0;i<farms;i++)
				last=last+c/(2+i*f);
			last=last+x/(((i)*f)+2);



			for(i=0;i<farms+1;i++)
				current=current+c/(2+i*f);
			current=current+x/(((i)*f)+2);

			if(last<current)
				break;
			farms++;
		}
		answer1=last;;
		dec=0;
		while(answer1!=0)
		{
			answer1/=10;
			dec++;
		}

		
		
		
		fout<<"Case #"<<size-1<<": ";
		fout<<fixed<<setprecision(7+dec)<<last<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}