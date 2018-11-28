#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <utility>
#include <functional>

#include <boost/algorithm/string.hpp>
#include <boost/foreach.hpp>

#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;


ifstream ifs;
ofstream ofs;
string buf;


long long gcd(long long P, long long Q){
	if (( P == 0 ) || ( Q == 0 ))
		return 0;
	
	while(P != Q){
		if (P > Q)
            P = P - Q;
		else
            Q = Q - P;
	}
	return P;
}


int main(int argc, char **argv){
    ifs.open("A-small-attempt0.in");
    ofs.open("A-small-attempt0.out");

    
	getline(ifs, buf);
	int T = atoi(buf.c_str());

	rep(i, T){
		getline(ifs, buf, '/');
	    long long P = atoll(buf.c_str());
        getline(ifs, buf);
        long long Q = atoll(buf.c_str());

        ofs << "Case #" << (i + 1) << ": ";
        long long gcdPQ = gcd(P, Q);
        long long P1 = P / gcdPQ;
        long long Q1 = Q / gcdPQ;
        if((Q1 & (Q1 - 1))){
            ofs << "impossible" << endl;
        }
        else{        
            int msbP1 = 0;
            long long tmpP1 = P1;
            while(tmpP1 != 0){
                msbP1++;
                tmpP1 >>= 1;
            }

            int msbQ1 = 0;
            long long tmpQ1 = Q1;
            while(tmpQ1 != 0){
                msbQ1++;
                tmpQ1 >>= 1;
            }

            int res = msbQ1 - msbP1;
            ofs << res << endl;
        }
        
	}
	

    ifs.close();
    ofs.close();
    return 0;
}

