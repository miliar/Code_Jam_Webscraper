#include <fstream>
#include <iostream>
#include <iomanip>

double calculateCookieTime(double C, double F, double X) {
    int farms=0;
    double time=0;
    while(true) {
        double rate=2+farms*F;
        double t_total=X/rate;
        double t_collect=C/rate;
        double t_rest=X/(rate+F);
        if(t_total<t_collect+t_rest) {
            return time+t_total;
        } else {
            ++farms;
            time+=t_collect;
        }
    }
}

int main() {
    std::ifstream infile("input.txt");
	std::ofstream outfile("output.txt");
    outfile<<std::setprecision(10);
	int testcases;
	infile>>testcases;

	double C, F, X;

	for(int i=1; i<=testcases; ++i) {
        infile>>C>>F>>X;
        outfile<<"Case #"<<i<<": "<<calculateCookieTime(C, F, X)<<std::endl;
	}

    return 0;
}
