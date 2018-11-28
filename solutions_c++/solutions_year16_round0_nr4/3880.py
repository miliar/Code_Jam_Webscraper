#include <fstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <set>
#include <iterator>
#include <map>
#include <cmath>
#include <queue>
#include <ctime>

using namespace std;


ifstream in("input.txt");
ofstream out("output.txt");

int t,k,c,s;

int main(int argc, const char * argv[]) {
    in >> t;
    int it=1;
    while (it<=t){
        out << "Case #" << it << ":";
        in >> k >> c >> s;
        if (k>s){
            out << " IMPOSSIBLE" << endl;
            it++;
            continue;
        }
        long long x = 1;
        for (int i=1;i<c;i++) x=x*k;
        long long p = 1;
        for (int i=1;i<=s;i++){
            out << " " << p;
            p+=x;
        }
        out << endl;
        it++;
    }
    
    return 0;
}