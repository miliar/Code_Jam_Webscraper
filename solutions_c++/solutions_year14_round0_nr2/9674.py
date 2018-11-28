#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("output.txt");

	unsigned int inputs=0;
	double C,G,F,X, answer=0, answer1=0;
	
	fin>>inputs;
	for(int i=0;i<inputs;i++)
	{
		answer=answer1=0;
		G=2;
		fin>>C>>F>>X;
		answer=X/G;
		for(int i=1;;i++)
		{
			for(int j=0;j<i;j++)
			{
				answer1+=C/G;
				G=G+F;
			}
			answer1+=X/G;
			if(answer<answer1)
				break;
			answer=answer1;
			answer1=0;
			G=2;
		}
		fout<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<answer<<endl;
	}


	fout.close();
	fin.close();
	system("pause");
	return 0;
}
