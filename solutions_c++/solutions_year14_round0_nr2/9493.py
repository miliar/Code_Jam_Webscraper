#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	int casenum = 0;
	float cost = 0;
	float fee = 0;
	float x = 0;
	float time = 0;
	int blimit = 0;
	char buffer[256];
	memset(buffer, 0, 256);
	ifstream infile("B-small-attempt0.in");
	ofstream outfile("result.out");
	if(!infile)
	{
		cout << "Unable to open infile" << endl;
		exit(1);
	}
	if(!outfile)
	{
		cout << "Unable to open outfile" << endl;
		exit(1);
	}
	
	infile.getline(buffer, 10);
	sscanf_s(buffer, "%d", &casenum);
	cout<<casenum<<endl;
	outfile.setf(ios::fixed );
	for(int i = 1; i <= casenum; i ++)
	{
		infile.getline(buffer, 100);
		sscanf_s(buffer, "%f %f %f", &cost, &fee, &x);
		blimit = ceill(x / cost - 2 / fee - 1);
		blimit = (blimit < 0) ? 0 : blimit;
		time = 0;
		for(int j = 0; j < blimit; j ++)
		{
			time += cost / (2 + j * fee);
		}
		time += x / (2 + blimit * fee);
		outfile<<"Case #"<<i<<": "<<setprecision(7)<<time<<endl;
	}
	infile.close();
	outfile.close();
}