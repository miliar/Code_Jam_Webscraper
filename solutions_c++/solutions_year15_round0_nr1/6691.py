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

long long process_testcase_A()
{
	long long smax;
	cin >> smax;
	
	string ss;
	cin >> ss;
	long long sum = 0;
	long long diff = 0;
	for (int req = 0; req < ss.length(); ++req) {
		long long fallingShort = req - sum;
		if (fallingShort > 0) {
			diff += fallingShort;
			sum += fallingShort;
		}
		sum += ss[req] - '0';
	}
	
	return diff;
}

long long process_testcase_B()
{
    long long A, B, K;
    cin >> A >> B >> K;
    if (A > B) {
        long long t = A;
        A = B;
        B = t;
    }
    K = min(K, A);
    //printf("%lld, %lld, %lld", A, B, K);
    long long rv = 0;
    for (long long i = 0; i < A; ++i) {
        for (long long j = 0; j < B; ++j) {
            rv += ((i&j) < K)? 1 : 0;
        }
    }
    return rv;
}

int main(int argc, char*argv[]) {
    int tc = 0;
	if(argc == 1) {
        freopen("inp.txt", "r", stdin);
        //freopen("outp.txt", "w", stdout);
    }
	else {
        freopen(argv[1], "r", stdin);
        //freopen("outp.txt", "w", stdout);
    }
    
	// find total number of testcases
	cin >> tc;
	
	// for every testcase
	for(int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ",i);
		cout << process_testcase_A();
        cout << endl;
	}
    
    return 0;
}