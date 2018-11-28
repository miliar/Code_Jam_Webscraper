#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
	ifstream fin("B-small-attempt0.in");
	cin.rdbuf(fin.rdbuf());
	ofstream fout("result.txt",ofstream::app|ofstream::out);
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		double C,F,X;
		cin>>C>>F>>X;
		double production=2.0;
		double totalTime=0.0;
		bool flag=1;
		while(flag)
		{
			double tNoFarm,tBuildFarm,tMoreFarm,tWithFarm;
			tNoFarm=X/production;
			tBuildFarm=C/production;
			tMoreFarm=X/(production+F);
			tWithFarm=tBuildFarm+tMoreFarm;
			if(tNoFarm<=tWithFarm)
			{
				totalTime+=tNoFarm;
				flag=0;
			}
			else 
			{
				totalTime+=tBuildFarm;
				production+=F;
				flag=1;
			}
		}
		fout.setf(ios::showpoint);
		fout.precision(7);
		fout.setf(ios::fixed);
		fout<<"Case #"<<i+1<<": "<<totalTime<<endl;
	}
	fout.close();
	fin.close();
	system("pause");
	return 0;
}