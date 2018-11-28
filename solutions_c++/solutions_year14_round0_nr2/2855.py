#include <fstream>

using namespace std;


ifstream in("input.txt");
ofstream out("output.txt");

int t;

void prs(int caseNum)
{
	double C, F, X;
	double sec = 0.0;
	double cps = 2.0;

	in >> C >> F >> X;

	while(true){
		if((double)(X / cps) <= (double)(C / cps) + (double)(X / (cps+F)) ){
			sec += (double)(X/cps);
			break;
		}else{
			sec += (double)C/cps;
			cps += (double)F;
		}
	}
	out.setf(out.fixed);
	out.precision(7);
	out << "Case #"<<caseNum <<": "<<sec <<endl;
}

int main()
{
	in >> t;

	for(int i = 0; i<t; i++){
		prs(i+1);
	}
	in.close();
	out.close();
}