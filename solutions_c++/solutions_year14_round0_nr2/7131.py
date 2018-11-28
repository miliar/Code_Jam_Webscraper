#include "cstdio"
#include <fstream>
#include <iostream>
using namespace std;
typedef long long i64;

int main() {
  ifstream infile;
  ofstream outfile;
  infile.open("B-large.in");
  outfile.open("a.out");
  int T = 0;
  infile >> T;
 
	double C;
	double F;
	double X;
	double cur;
	double produce;
	double time;
	double bestTime;

for (int Ti = 1; Ti <= T; ++Ti) {
	infile >> C >> F >> X;
	cur = 0.0f;
	produce = 2.0f;
	time = 0.0f;
	bestTime = X;
	while(1)
	{
		if(Ti == 4)
		{
			cout << "C " << C << ", F " << F << ", X " << X << ", Cur " << cur << ", Produce " << produce << ", Time " << time << ", " << C/produce << ", " << X/produce <<  endl;
		}
		bestTime = time + X/produce;
		if( C/produce > X/produce )
		{
			//time += X/produce;
			break;
		}
		else
		{
			time += C/produce;
			cur += produce;
			produce += F;
		}
		
		if(time + X/produce > bestTime)
			break;
	}
	
	char buf[64];
	sprintf(buf,"Case #%d: %.7f\n",Ti, bestTime);
	outfile << buf;
  }
  infile.close();
  outfile.close();
  return 0;
}