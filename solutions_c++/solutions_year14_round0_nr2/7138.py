/*
ID: devraj.2
PROG: ride
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
const static string filename ="B";
#define EPSILON 0.00001

string Solve()
{

	
	stringstream sout;
	double c = 0,f =0, x =0;
	double cur_x =0, cur_t =0 ,f_cur = 2;
	cin>>c>>f>>x;
	while(cur_x < x || (fabs(cur_x - x) > EPSILON))
	{
		double farm_rate = c / f_cur;
		double time1 = farm_rate + x /(f_cur+f);
		double time2 = x / f_cur;
		if(time2 < time1 )
		{
			cur_t += time2;
			cur_x = x;
		}
		else
		{
			cur_t += farm_rate;
			f_cur += f;
			cur_x = 0;
		}

	}
	sout.precision(7);
	sout<< fixed <<cur_t;
	return sout.str();
}


void SolveSmall()
{
	//A-small-attempt0
	string inFile = filename + "-small" +"-attempt0"+ ".in" ;
	string outFile = filename + "-small"+"-attempt0" + ".out";

	freopen(outFile.c_str()  ,"w",stdout);
	freopen(inFile.c_str() ,"r", stdin);

}

void SolveLarge()
{
	string inFile = filename + "-large"  + ".in" ;
	string outFile = filename + "-large" + "-attempt0" + ".out";

	freopen(outFile.c_str()  ,"w",stdout);
	freopen(inFile.c_str() ,"r", stdin);


}

int main()
{
		//SolveSmall();
		SolveLarge();
		int t_testCase = 0;
		cin>>t_testCase;

		for(int t = 0; t < t_testCase; ++t)
		{
			cout<<"Case #"<<t+1<<": "<<Solve()<<endl;

		}

    return 0;
}