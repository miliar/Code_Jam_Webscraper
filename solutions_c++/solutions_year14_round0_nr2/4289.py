//
//  main.cpp
//
//  Created by Vichare, Vivek on 4/12/14.
//

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;
typedef vector <int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef long double ld;

ll process_testcase_A(ifstream &is)
{
	string s;
	getline(is,s);
	istringstream iss(s);
    ld C, F, X;
    iss >> C >> F >> X;

    ld rv = 0;
    ld curRate = 2;// per second
    rv = X/curRate;// this is the tme it's gonna take to reach X cookies at current rate
    
    ld numFarms = 0;
    ld elapsedTime = 0;
    curRate = 2 + numFarms*F;
    ld timeToNextDecisionPoint = C/curRate; // we need to make the next decision when we have C cookies to buy another farm
    while ((elapsedTime + timeToNextDecisionPoint) < rv) {
        elapsedTime += timeToNextDecisionPoint; // since we have reached the decision point, the elapsed time moves forward
        ld timeToXWithNewFarm = elapsedTime + X/((ld)2 + F*(numFarms+(ld)1));
        if (timeToXWithNewFarm > rv) {
            break;
        }
        // else
        ++numFarms;
        curRate = (ld)2+F*numFarms;
        rv = timeToXWithNewFarm;
        timeToNextDecisionPoint = C/curRate;
    }
    cout <<std::fixed << setprecision(7) << rv;
    
    return 0;
}

int main(int argc, char*argv[]) {
    int tc = 0;
	ifstream is;
	if(argc == 1)
		is.open("inp.txt");
	else
		is.open(argv[1]);
		
	// find total number of testcases
	string s;
	getline(is,s);
	istringstream iss(s);
	iss >> tc;
	
	// for every testcase
	for(int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ",i);
		process_testcase_A(is);
        cout << endl;
	}
	is.close();
    
    return 0;
}