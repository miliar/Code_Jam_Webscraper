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


long long process_testcase_A(ifstream &is)
{
	// find first
	string s;
    
    // get f
	getline(is,s);
	istringstream iss(s);
    int f;
	iss >> f;
    
    vvi fArrangement;
    vi candidates;
    for (int i = 0; i < 4; ++i) {
        getline(is,s);
        if (i+1 != f) {
            continue;
        }
        istringstream issrow(s);
        for (int j = 0; j < 4; ++j) {
            int num;
            issrow >> num;
            candidates.push_back(num);
        }
        // can't break. we need to consume those lines
    }
    
    for (int i = 0; i < 4; ++i) {
        //cout << " " << candidates[i];
    }
    
    // get s
	getline(is,s);
	istringstream iss2(s);
    int sec;
	iss2 >> sec;
    vi seCandidates;

    int numHits = 0;
    int soln = -1;
    for (int i = 0; i < 4; ++i) {
        getline(is,s);
        if (i+1 != sec) {
            continue;
        }
        istringstream issrow(s);
        for (int j = 0; j < 4; ++j) {
            int num;
            issrow >> num;
            seCandidates.push_back(num);
            for (int k = 0; k < 4; ++k) {
                if (num == candidates[k]) {
                    numHits++;
                    soln = num;
                }
            }
        }
        // can't break. we need to consume those lines
    }

    //cout << "\n [" << sec << "] :" ;
    for (int i = 0; i < 4; ++i) {
        //cout << " " << seCandidates[i];
    }

    if (0 == numHits) {
        cout << "Volunteer cheated!";
    } else if (1 == numHits) {
        cout << soln;
    } else {
        cout << "Bad magician!";
    }

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