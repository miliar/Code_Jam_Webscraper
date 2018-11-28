#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;
int main()
{
	double ps,c,f,x,y,cookies;
	int n;
	ifstream fin ("C:\\file\\co.in");
	ofstream fout ("C:\\file\\co.out");
	fin>>n;
	for(int i = 0 ; i<n;i++)
	{
		y=0;
		ps=2;
		fin>>c;
		fin>>f;
		fin>>x;
		for(;;)
		{
			if((x/ps)-(x/(ps+f))>(c/ps))
			{
				y+=c/ps;
				ps+=f;
			}
			else
				break;
		}
		y+=(x/ps);
		fout<<"Case #"<<(i+1)<<": ";
		fout<<setprecision(7)<<fixed<<y;
		if((i+1)!=n)
			fout<<endl;
		
	}
	return 0;
}