//
//  main.cpp
//  GCJ2013QAC
//
//  Created by Seki Inoue on 2013/04/13.
//
//

//
//  This code uses project templates developed by peroxyacyl.
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

typedef unsigned long long ull;
typedef long double ld;

const static string kProblemSet = "small";

ull reversenum(ull num) {
    ull rev = 0;
    while (num) {
        int last = num%10;
        rev = rev*10+last;
        num /= 10;
    }
    return rev;
}

bool isFair(ull num) {
    return (num == reversenum(num));
}
/*
ull nextFS(ull num) {
    if (num == 0) return 1;
    ull sqr = sqrt((ld)num)+1;
    int dig = log10(sqr);
    ull next = 0;
    
    if (!(dig%2)) {
        int halfd = pow(10, dig/2);
        ull upper = sqr/halfd-1;
        while (next < sqr || !isFair(next*next)) {
            upper++;
            next = upper*(halfd) + reversenum(upper/10);
        }
    }else {
        int halfd = (pow(10, (dig+1)/2));
        ull upper = sqr/halfd-1;
        while (next < sqr || !isFair(next*next)) {
            upper++;
            next = upper*halfd + reversenum(upper);
        }
    }
    return next*next;
}
*/
int main(int argc, const char * argv[]) {
    ifstream ifs( kProblemSet + ".in" );
    ofstream ofs( kProblemSet + ".out" );
	int T = 0;
	ifs >> T;
    
    
//    for (int i = 1; i <= 1000; i++) {
//        cout << i*i << ":" << (isFair(i)&&isFair(i*i)) << endl;
//    }
    
    
    
    for (int testCase = 0; testCase < T; testCase++) {
        
        ull begin, end;
        ifs >> begin >> end;
        //cout << begin << ":" << end;
        int pa = 0;
        ull sqb = sqrt(begin);
        ull sqe = sqrt(end);
        
        for (ull i = sqb; i <= sqe; i++) {
            if (isFair(i) && isFair(i*i) && i*i >= begin && i*i<=end) {
                pa++;
            }
        }
        cout << "Case #" << testCase+1 << ": " << pa << endl;
        ofs << "Case #" << testCase+1 << ": " << pa << endl;
    }
    
	return 0;
}
