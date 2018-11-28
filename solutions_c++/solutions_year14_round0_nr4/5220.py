
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
typedef long double ld;
typedef vector<ld> vld;

long long process_testcase(ifstream &is)
{
	// find total number of testcases
	string s;
    
	getline(is,s);
	istringstream iss(s);
    int N;
	iss >> N;

    // Naomi
    vld naomisWeights(N);
	getline(is,s);
    istringstream isnaomi(s);
    for (int i = 0; i < N; ++i) {
        isnaomi >> naomisWeights[i];
    }

    // Ken
	getline(is,s);
    istringstream isken(s);
    vld kensWeights(N);
    for (int i = 0; i < N; ++i) {
        isken >> kensWeights[i];
    }
    
    sort(naomisWeights.begin(), naomisWeights.end());
    sort(kensWeights.begin(), kensWeights.end());

    long long warsWonWithoutDeceit = N;
    vld::iterator kensCandidate = kensWeights.begin();
    for (vld::iterator naomisCandidate = naomisWeights.begin(); naomisCandidate != naomisWeights.end(); ++naomisCandidate) {
        for ( ; kensCandidate != kensWeights.end(); ++kensCandidate) {
            if (*kensCandidate > *naomisCandidate) {
                --warsWonWithoutDeceit; // Naomi lost this battle
                ++kensCandidate;
                break;
            }
        }
        if (kensCandidate == kensWeights.end()) {
            break; // Ken has no more winners
        }
    }
    
    long long deceitfulVictories = 0;
    for (vld::iterator naomisCandidate = naomisWeights.begin(), kensCandidate = kensWeights.begin(); naomisCandidate != naomisWeights.end(); ++naomisCandidate) {
        if (*naomisCandidate > *kensCandidate) {
            // naomi wins this battle
            ++deceitfulVictories;
            ++kensCandidate;
        }
    }

    cout << deceitfulVictories << " " << warsWonWithoutDeceit;
    
    return 0;
}

int main(int argc, char*argv[]) {
    int tc = 0;
	ifstream is;
    if (argc != 2) {
        cout << "./a.out input.filename\n";
        exit(1);
    }
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
		process_testcase(is);
        cout << endl;
	}
	is.close();
    
    return 0;
}