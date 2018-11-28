#include <algorithm>
#include <cstdarg>
#include <cstddef>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <memory>
#include <set>
#include <vector>
#include <intrin.h>
#include <exception>
#include <assert.h>
#include <set>
#include <string>
#include <chrono>
#include <sstream>
#include <bitset>
#include <list>
#include <deque>

#include <boost/multiprecision/integer.hpp>

using namespace std;

typedef int64_t i64;
typedef uint64_t u64;
typedef int32_t i32;
typedef uint32_t u32;
typedef boost::multiprecision::int128_t i128;
typedef boost::multiprecision::uint128_t u128;
typedef boost::multiprecision::int256_t i256;
typedef boost::multiprecision::uint256_t u256;
typedef boost::multiprecision::int512_t i512;
typedef boost::multiprecision::uint512_t u512;
typedef boost::multiprecision::int1024_t i1024;
typedef boost::multiprecision::uint1024_t u1024;

#define F(i,a) for(size_t (i)=0;(i)<(a);++(i))
#define R(i,a) for(i64 (i)=((a));(i)>=0;--(i))
#define D(i,a,b) for(size_t (i)=(a);(i)<(b);++(i))
#define E(i,a) for(auto (i)=(a).begin();(i)!=(a).end();++(i))
#define V vector
#define VI V<int>
#define VVI V<V<int>>
#define VL V<i64>
#define VVL V<V<i64>>
#define ALL(a) (a).begin(),(a).end()
#define VS V<string>
#define P pair
#define MP make_pair

#define DEBUG 0

int proc(int m, const string& s){
	int n=0, res=0;
	F(i,s.size()){
		n += s[i]-48;
		while(n<=i) {++res; ++n;}
	}
	return res;
}

//A 2015
int main(int argc, char** argv){
	string fs;
#if DEBUG==1
	fs = "a2015";
#else
	fs = *(++argv);
#endif
	string infile = "C:/gcj/" + fs + ".txt";
	string outfile = "C:/gcj/" + fs + "_out.txt";
	ifstream fi(infile.c_str());
	ofstream fo(outfile.c_str());

	cout << "Running " << infile << endl;

	int t,m;
	fi >> t;
	string s;
	F(i, t){
		fi >> m;
		fi >> s;
		fo << "Case #" << i + 1 << ": " << proc(m,s) << endl;
		cout << "Case #" << i+1 << " complete" << endl;
	}

	fo.flush();
	fo.close();
	fi.close();
	return 0;
}