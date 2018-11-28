#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <memory.h>
#include <fstream>
#include <stdio.h>
#include <vector>
#include <math.h>
#include <iomanip>
#include <cmath>
#include <limits>
using namespace std;




int main(){

	ofstream myfile;
	myfile.open ("/Users/mac/Desktop/out.txt");
    ifstream filein ("/Users/mac/Desktop/B-small-attempt0.in.txt");
    int t;
    double C,F,X;
    
    filein >> t;
    

    for(int T=1;T<=t;T++) {
    	filein >> C >> F >> X;
        double tot = 0;
        double produce = 2;
        while(true) {
            double finish = X/produce;
            double wait = (C/produce) + (X/(produce+F));
            if(wait < finish) {
                tot += C/produce;
                produce += F;
            }else {
                tot += finish;
                break;
            }
        }   
        myfile << fixed << setprecision(7);
    	myfile << "Case #" << T << ": " << tot << endl;
    }
    
	  myfile.close();

}