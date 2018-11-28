#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
	int casenum;
	int count;
	long double result;
	long double speed;
	long double c,f,x;
	ofstream fout;
	fout.open("c://output.out");
	ifstream fin; 
	fin.open("c://input.in");
	fin>>casenum;
	for(int num=1;num<=casenum;num++)
	{
		speed=2;
		result=0;
		fin>>c>>f>>x;
		fout<<"Case #"<<num<<": ";

		while(x/speed>(c/speed+x/(speed+f)))
		{
			result+=c/speed;
			speed+=f;
		}
		result+=x/speed;



		fout << fixed << setprecision(7) << result << endl; 







	}

	
	return 0;
}