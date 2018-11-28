#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("B_output.txt");

int n;

double C, F, X;
double tot;

void proc(int ca)
{
	tot = X/2;
	double earn = 2;
	double time = 0;
	while (1){
		if ((X / earn < (C / earn + C / (earn + F)) 
			|| ((time+X/earn) > tot))){

			fout.setf(ios::fixed);
			fout.precision(7);
			fout << "Case #" << ca+1 << ": " << tot << endl;
			break;
		}
		if (tot > time + (X / earn)){  //X를 만들면서 최소시간 기록
			tot = time + (X / earn);
		}

		time += C / earn;
		earn += F;

		
		
		
	}

	return;
}


void main()
{
	fin >> n;
	for (int i = 0; i < n; i++){
		fin >> C >> F >> X;
		proc(i);
	}

}