//
//  main.cpp
//  GCJ20151BA
//
//  Created by Seki Inoue on 5/3/15.
//  Copyright (c) 2015 Seki Inoue. All rights reserved.
//

//
//  This code is powered by peroxyacyl's GCJ Template for Xcode.
//  https://github.com/peroxyacyl/gcj-xcode-template
//


#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;



const static string kProblemSet = "small";

unsigned long long rev(unsigned long long n) {
    
    string s = to_string(n);
    reverse(s.begin(), s.end());
    return stoi(s);
}


int main(int argc, const char * argv[]) {
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );

    const unsigned long long M = 1000001;
    unsigned long long map[M] = {0};
    map[0] = 0;
    
    queue<pair<long, unsigned long long> > q;
    q.push(make_pair(1, 1));
    while (q.size()) {
        pair<long, unsigned long long> i = q.front();
        q.pop();
        if (i.second < M && ( map[i.second] == 0 || map[i.second] > i.first)) {
            map[i.second] = i.first;
            
            q.push(make_pair(i.first+1, i.second+1));
            q.push(make_pair(i.first+1, rev(i.second)));
            
        }

    }
    
    
    
	int T = 0;
    
	ifs >> T;
    
    for (int testCase = 0; testCase < T; testCase++) {
        
        int N = 0;
        ifs >> N;
        
        cout << "Case #" << testCase+1 << ": " << map[N] << endl;
        ofs << "Case #" << testCase+1 << ": " << map[N] << endl;
    }
    
	return 0;
}
