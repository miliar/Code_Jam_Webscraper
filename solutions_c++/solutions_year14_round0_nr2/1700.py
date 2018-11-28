#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <iomanip>
using namespace std;

int main(int argc, char const *argv[])
{
	ifstream infile("B-large.in");
	ofstream outfile("B-large-out.ot");
	int N = 0;
	infile >> N;
    outfile<< setprecision(7) << fixed;
    for(int i = 1; i <= N; ++i){
    	double C = 0;
    	double F = 0;
    	double X = 0;
    	infile >> C >> F >> X;

    	double S = 2;
        double totalTime = 0;
        double twith = X/S;
        double tout = C/S + X/(S+F);
        while(tout < twith){
            totalTime += C/S;
            S += F;
            tout = C/S + X/(S+F);
            twith = X/S;
        }
        totalTime += X/S;
        outfile << "Case #" << i << ": " << totalTime;
        if(N != i)
        	outfile << "\n";
    }
    infile.close();
    outfile.close();
    return 0;
}
	
