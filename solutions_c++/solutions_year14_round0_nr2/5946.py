#include <iostream>
#include <vector>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
using namespace std;



double getRes(double c, double f, double x){
    double T=0;
    vector<double> fc;
    vector<double> xc;

    int n=0;
    fc.push_back(0);
    xc.push_back(x/2.0);
    T = xc[0];
    while (true){
        n++;
        fc.push_back(fc[n-1]+c/(2.0+(n-1)*f));
        xc.push_back(x/(2.0+n*f));

        if (fc[n]+xc[n]>=T){
            return T;
        }else{
            T = fc[n]+xc[n];
        }
    }
}


int main()
{
     //ifstream input("A-small-practice.in");
    //ofstream output("A-small-practice.txt");
    ifstream input("B-large.in");
    ofstream output("out_l.txt");
    //ifstream input("A-large-practice.in");
	//ofstream output("A-large-practice.txt");
	string line;
	int casenum;
	input >> casenum;
    for (int i=0;i< casenum;i++){
        double c,f,x;

        input >> c;
        input >> f;
        input >> x;

        output.precision(10);
        output << "Case #" << i+1 <<": " << getRes(c,f,x) << endl;

    }
    input.close();
    output.close();
    return 0;
}

