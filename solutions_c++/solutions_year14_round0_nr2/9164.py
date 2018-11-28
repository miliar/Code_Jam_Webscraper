#include <iostream>
#include <cstdlib>
#include <fstream>
#include <iomanip>
using namespace std;

double cal(double c, double f, double x, int num_farm){
    double deno = 2;
    double result = 0.0;
    for(int i = 0 ; i < num_farm; i++){
        result += c/deno;
        deno += f;
    }
    result += x/deno;
    return result;
}

int main() {
    ofstream ofile;
    ofile.open ("output.txt");

    ifstream ifile;
    ifile.open("input.txt");

	int test;
	double c;
	double f;
	double x;
	double result = 0.0;
	ifile >> test;
	for(int t = 1; t <= test; t++){
        ifile >> c >> f >> x;
        int num_farm = 0;
        result = x;
        double next = cal(c,f,x,num_farm);
        while(result > next){
            result = next;
            next = cal(c,f,x,++num_farm);
        }
        ofile << setprecision(7) << fixed;
        ofile << "Case #" << t << ": " << result << endl;
	}
	ifile.close();
	ofile.close();
	return 0;
}
