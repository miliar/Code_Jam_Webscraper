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

long double naomi[2002];
long double ken[2002];

typedef enum {NAOMI, KEN} tWho;
typedef pair<long double, tWho> pldwho;

pldwho both[4004];

bool pldwhoCompare(pldwho x, pldwho y) {
    return x.first < y.first;
}

long long process_testcase_D(ifstream &is)
{
	// find total number of testcases
	string s;
    
    // get N
	getline(is,s);
	istringstream iss(s);
    int N;
	iss >> N;
    
    // get naomi's weights
	getline(is,s);
    istringstream isnaomi(s);
    for (int i = 0; i < N; ++i) {
        isnaomi >> naomi[i];
        both[2*i] = pldwho(naomi[i], NAOMI);
    }

    // get naomi's weights
	getline(is,s);
    istringstream isken(s);
    for (int i = 0; i < N; ++i) {
        isken >> ken[i];
        both[2*i+1] = pldwho(ken[i], KEN);
    }
    
    sort(naomi, &naomi[N]);
    sort(ken, &ken[N]);
    sort(both, &both[2*N], pldwhoCompare);

    /*
    cout << "\nNaomi: ";
    for (int i = 0; i < N; ++i) {
        cout << naomi[i] << " ";
    }
    cout << "\nKen  : ";
    for (int i = 0; i < N; ++i) {
        cout << ken[i] << " ";
    }

    cout << "\nBoth : ";
    for (int i = 0; i < 2*N; ++i) {
        cout << both[i].first << " ";
    }
     */

    long long warN = 0;
    for (int i = 0; i < 2*N; ++i) {
        if (both[i].second == NAOMI) {
            ++warN;
        } else if (warN > 0) {
            --warN;
        }
    }
    
    //cout << "\nIn war, Naomi would have won: " << warN << " games\n";
    
    long long decWarN = 0;
    for (int i = 0, j = 0; i < N; ++i) {
        if (naomi[i] < ken[j]) {
            // naomi lost this...which means ++i
            // ken lost his highest weight block. which isn't worth keeping track of
        } else {
            // naomi can win this
            ++decWarN;
            ++j;
        }
    }
    //cout << "\nIn Dwar, Naomi would have won: " << decWarN << " games\n";

    
    cout << decWarN << " " << warN;
    
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
		process_testcase_D(is);
        cout << endl;
	}
	is.close();
    
    return 0;
}