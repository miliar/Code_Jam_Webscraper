#include <iostream>;
#include <fstream>;

using namespace std;

ifstream infile;
ofstream outfile;

int n,k;
double c,f,x;

void calculate() {

	double speed=2;
	double time=0;
	
	while (x/speed>=c/speed+x/(speed+f)) { time=time+c/speed; speed=speed+f; }
	time=time+x/speed;
	
	outfile<<"Case #"<<k+1<<": "<<time<<endl;

}


int main() {

	infile.open("input.txt");
	outfile.open("output.txt");
	outfile.precision(15);

	infile>>n;

	for (k=0; k<n; k++) {
		infile>>c>>f>>x;
		calculate();
	}

}