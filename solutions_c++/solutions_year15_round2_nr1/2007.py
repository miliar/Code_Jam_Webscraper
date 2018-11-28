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
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;


long reverse(long x) {
    long newN =0, left =0;
    while(x != 0)  {
        left = x%10;
        newN = newN*10 + left;
        x = x/10;
    }
    return newN;
}

//opt(i) = {i, i+1, ..., n} min count
//opt(i) = 1 + opt(i+1) || opt(flip(i))
//opt(n) = 0;
long minCount(long n) {
    vector<long> opt(n+1, 0);
    opt[n] = 1;
    for(long i=n-1; i>=1; --i) {
        long opt_next = 1 + opt[i+1];
        long flip_num = reverse(i);
        if(flip_num > i && flip_num <= n) {
            long opt_flip = 1 + opt[flip_num];
            opt[i] = opt_next < opt_flip ? opt_next : opt_flip;
        } else {
            opt[i] = opt_next;
        }
    }
    
    return opt[1];
}

long minCount1(long n) {
    long cur = 1;
    long count = 0;
    
    while(cur < n) {
        count++;
        long numr = reverse(cur);
        if(numr > cur && numr <= n
           ) {
            cur = numr;
        } else {
            cur = cur+1;
        }
    }
    
    return ++count;
    
}

int main() {
    ifstream infile;
    ofstream outfile;
    
    infile.open("A-small-attempt1.in");
    outfile.open("A-small-attempt1.out");
    
    int T;
    infile >> T;
    for(int i=0; i<T; ++i) {
        long N = 0;
        infile >> N;
        long count = minCount(N);
        
        outfile << "Case #" << i+1 << ": " << count << endl;
    }
    
    infile.close();
    outfile.close();
    return 0;
}

