//
//  main.cpp
//  googlecodejam
//
//  Created by Yoshioka Tsuneo on 4/12/14.
//  Copyright (c) 2014 Yoshioka Tsuneo. All rights reserved.
//

#include <fstream>
#include <iostream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>
#include <sstream>
#include <queue>
#include <stdexcept>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cassert>
#include <unistd.h>
#include <string.h>

#include <stack>

#define decltype(X) __typeof(X)
#define REP(i, n) for(int i=0; i<(int)n; i++)
#define FOR(it, c) for(decltype((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define ALL(c) (c).begin(), (c).end()

#define EPS 0.000001
using namespace std;

typedef long long ll;


set<int> get_num_set(istream &in)
{
    int ans_row;
    in >> ans_row;
    set<int> chosen_set;
    for(int r=0;r<4;r++){
            for(int c=0;c<4;c++){
                int num;
                in >> num;
                if(r+1 == ans_row){
                    chosen_set.insert(num);
                }
            }
    }
    return chosen_set;
}

string testcase(istream &in, int t)
{
    set<int> s1 = get_num_set(in);
    set<int> s2 = get_num_set(in);
    
    
    vector<int> result;
    set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), back_inserter(result));
    
    if(result.size()==1){
        stringstream ss;
        ss << result[0];
        return ss.str();
    }else if(result.size()==0){
        return "Volunteer cheated!";
    }else{
        return "Bad magician!";
    }
}

int main(int argc, const char * argv[])
{
    // insert code here...
    ios::sync_with_stdio(false);
    cin.tie(0);

    string fname = "/dev/stdin";
    if(argc>=2){
        fname = argv[1];
    }
    ifstream in(fname);
    if(!in){
        cout << "File open error:" << fname << endl;
        exit(1);
    }
    int T;
    in >> T;
    for(int t=0;t<T;t++){
        auto result = testcase(in, t);
        cout << "Case #" << t+1 << ": " << result << endl;
    }
    
    // std::cout << "Hello, World!\n";
    return 0;
}


