#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int T;
    double C, F, X;
    fin >> T;
    
    for (int t = 1 ; t <= T; t++)
    {   
        fin >> C >> F >> X;

		double n = (X-C)/C * F;

		double start = 2.0;
		double answer = 0.0;
		while (start < n){
			answer += C / start;
			start += F;			
		}		
		answer += X / start;
       cout.precision(10);
       fout << setprecision(10) << "Case #" << t << ": " << answer << endl;
    }
}
