#include <algorithm>
#include <bitset>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <queue>
// q.push(el);
// q.front(); q.pop(); 

#include <sstream>
// ostringstream buf;

#include <cstdio>
// sscanf(time.c_str(), "%d:%d:%d", &H, &M, &S);

#include <limits>
// std::numeric_limits<long long>::max();

typedef long long ll;
#include <fstream>
#include "quaternion.hpp"
typedef ::boost::math::quaternion<int> qType;

const qType e(1,0,0,0);
const qType i(0,1,0,0);
const qType j(0,0,1,0);
const qType k(0,0,0,1);


qType decode(const char c) {
    if (c=='i')
	return i;
    else if (c=='j')
	return j;
    else if (c=='k')
	return k;
    assert(false);
}

qType prod_bf(std::vector<qType> v, int a, int b) {
    qType p = e;
    for (int m=a; m<b; m++) {
	p = p*v[m];
    }
    return p;
}

bool one_step(std::ifstream& fin) {
    	ll L;
	fin >> L;
	ll X;
	fin >> X;

	std::string s;
	fin >> s;
	std::vector<qType> v;
	while (X--) {
	    for (auto c : s) {
		v.push_back(decode(c));
	    }
	}

	std::vector<qType> prod(v.size()+1);
	{
	    qType p = e;
	    prod[0] = p;
	    for (int m = 0; m<v.size(); m++) {
		p = p*v[m];
		prod[m+1] = p;
	    }
	}

	std::vector<qType> prev(v.size()+1);
	{
	    qType p = e;
	    prev[0] = p;
	    for (int m = 0; m<v.size(); m++) {
		p = pow(v[m], -1)*p;
		prev[m+1] = p;
	    }
	}

	// for (int a=0; a<v.size(); a++)
	//     for (int b=a; b<=v.size(); b++) {
	// 	assert(prod_bf(v, a, b) == prev[a] * prod[b]);
	//     }

	int a = 1;
	int b = v.size()-1;

	while (true) {
	    if (a>=v.size() || a>b)
		return false;

	    if (prod[a] != i) {
		a++;
		continue;
	    }

	    if (prev[b] * prod[v.size()] != k) {
		b--;
		continue;
	    }

	    if (prev[a] * prod[b] == j)
		return true;
	    else {
		a ++ ;
		b --;
	    }
		
	}
	return false;
}



// g Csmall.cpp -Wno-deprecated -I/usr/include/boost/math/
int main() {

    std::ifstream fin ("Csmall.in");    

    int T;
    fin >> T;
    for (int icase=1; icase<=T; icase++) {
	auto ans = one_step(fin);
	if (ans)
	    std::cout << "Case #" << icase << ": YES\n";
	else
	    std::cout << "Case #" << icase << ": NO\n"; 
    }
}
