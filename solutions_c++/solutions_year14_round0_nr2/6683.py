#include <iostream>
#include <iomanip>
//#include <cstdio>
#include <algorithm>
#include <fstream>

using namespace std;

double calc_time(double c, double f, double x)
{
	double cur_time = 0, cur_rate = 2, pos1, pos2;
	while(true)
	{
		pos1 = cur_time + x/cur_rate;
		pos2 = cur_time + c/cur_rate + x/(cur_rate + f);
		if(pos1 < pos2)
			break;
		cur_time+= (c/cur_rate);
		cur_rate+=f;
	}
	return pos1;
}


int main()
{
	ifstream in;
	ofstream out;
	int t;
	double c, f, x;
	in.open("B-large.in");
	out.open("out2l.txt");
	in>>t;
	int count=1;
	
	while(t--)
	{
		in>>c>>f>>x;
		out<<"Case #"<<count<<": "<<fixed<<setprecision(7)<<calc_time(c, f, x)<<endl;
		count++;
	}
	
	in.close();
	out.close();
	return 0;
}
