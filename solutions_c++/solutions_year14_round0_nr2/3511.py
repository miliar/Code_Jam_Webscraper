/*
 * purpose: a template backbone for CodeJam solution
 * created: 2014-03-15
 * revised: 2014-03-29
 * author: Hoffman Tsui
 * 
 * start time: 11:07
 * end time: 11:00
 * read time: 11:15
 * idea: 11:30
 * study float/double: 12:05
 * start code: 12:15
 * end code: 13:21 (test cases succeed except case 3)
 * time to completion: n min(s)
 */

#include <unistd.h>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <iomanip>


void help();

bool AlmostEqualRelative(double A, double B, double maxRelDiff) {
    double diff = fabs(A - B);
    A = fabs(A);
    B = fabs(B);
    // Find the largest
    double largest = (B > A) ? B : A;

    if (diff <= largest * maxRelDiff)
        return true;
    return false;
}

double next_time(double C, double F, double X, double& cf, bool& finish) {
    std::cout << std::fixed << std::setprecision(7) ;
    //std::cout << std::fixed << std::setprecision(7) <<  "C = " << C << ", F = " << F << ", X = " << X << std::endl;
    double w_t, b_t;
    w_t = X / cf;
    b_t = X / (cf + F) + C / cf; 
    //std::cout << "w_t = " << w_t << ", b_t = " << b_t ;
    if ( AlmostEqualRelative( w_t, b_t, 0.0000001 )) {
        finish = true;
        //std::cout << " , relatively equal, add time: " << w_t << std::endl;
        return w_t;
    } else if ( b_t < w_t ) {
        double tmp = C / cf;
        cf += F;
        //std::cout << " , buy a farm, add time: " << tmp << std::endl;
        return tmp;
    } else {
        finish = true;
        //std::cout << " , wait to succeed, add time: " << w_t << std::endl;
        return w_t;
    }
}

int main (int argc, char *argv[]) {
    int c;
    const char* in_file;
    //const char* out_file;
    while (( c = getopt(argc, (char **)argv, "f:h:?")) != -1) {
        char flag = (char)c;
        switch(flag) {
            case 'f':
                in_file = optarg;
                break;
            default:
                help();
        }
    }
    
    // declar data structure
    
    // read content from file, close the stream when finish
    std::ifstream is(in_file);
	if (!is) {
		return 2;
    } else {
        // load into data structure
        int T;
        double C, F, X;
        std::string line;
        is >> T;
        getline(is, line);
        for (int c=1; c<=T; c++) {
            std::stringstream ss;
            getline(is, line);
            ss << line;
            ss >> C;
            ss >> F;
            ss >> X;
            //std::cout << "line = " << line << std::endl;
            //std::cout << "C = " << C << ", F = " << F << ", X = " << X << std::endl;
            bool done = false;
            double tot = 0;
            double cf = 2;
            do {
                tot += next_time(C, F, X, cf, done);
                //std::cout << "tot=" << tot << std::endl;
            } while (!done);
            std::cout << "Case #" << c << ": " << std::fixed << std::setprecision(7) << tot << std::endl;
            //ss.str(std::string()); // clear stringstream
        }
    }
	is.close();

	return 0;
}

void help() {
    std::cerr << "Usage: command [-f filename]" << std::endl;
}
