#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <climits>
#include <math.h>


using namespace std;

int main()
{
    ifstream input;
	//input.open("input.txt");
	input.open("A-small-attempt0.in");

	ofstream output("out.txt");
	int casenum;
    input >> casenum;

    //for each case
	for (int k=0;k<casenum;k++){
        long double r = 0;
        long double t = 0;
        long double res = 0;
        input >> r;
        input >> t;
         //long double nb = -2*r+1;
         //long double b2 = (2*r-1)*(2*r-1);
         //long double ac = 8*t;
         //long double bac = b2+ac;
         //bac = sqrt(bac);
         //res = long(floor(nb+bac)/4);
         res = long ((-2*r+1 + sqrtl((2*r-1)*(2*r-1)+8*t))/4);

        //long double aaa = 2*(res)*(res)+(2*r-1)*(res);
        //long double aaa = 2*(res+1)*(res+1)+(2*r-1)*(res+1);
         //cout << "aaa" << aaa << endl;

         if ((2*(res-1)*(res-1)+(2*r-1)*(res-1))>=t){
             res--;
         }

        output<< std::fixed;
        output.precision(0);
        output << "Case #" << k+1 << ": " <<res <<endl;


	}

    input.close();
    output.close();
    return 0;
}
