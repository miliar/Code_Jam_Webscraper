#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;
int main()
{	ofstream fout;
	fout.open("jam2ans.txt");
	setprecision(20);
	int cases,ca=1;
	cin>>cases;
	while(cases-->0)
	{	double c,f,x,c1,f1,x1,sum2=0,sum1=0;
		cin>>c>>f>>x;
		c1=c;f1=2;x1=x;
		if(x<=c)
		{	
			fout<<std::setprecision(10)<<"Case #"<<ca<<": "<<x/2<<endl;
		}
		else
		{
			while(1)
			{	
				
				if((x/f1)<((c/f1)+(x/(f+f1))))
				{
					sum1+=x/f1;
					break;
				}
				sum1+=c/f1;
				f1+=f;

				
			}
		fout<<std::setprecision(10)<<"Case #"<<ca<<": "<<sum1<<endl;	
		}
		ca++;
	}
	return 0;
}
