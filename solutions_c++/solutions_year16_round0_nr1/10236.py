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
#include <boost/multiprecision/cpp_bin_float.hpp>
#include <boost/multiprecision/cpp_int.hpp>

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
typedef boost::multiprecision::cpp_bin_float_quad quad;
typedef boost::multiprecision::cpp_int mi;


#define F(i,a) for(i64 (i)=0;(i)<(a);++(i))
#define R(i,a) for(i64 (i)=((a));(i)>=0;--(i))
#define D(i,a,b) for(i64 (i)=(a);(i)<(b);++(i))
#define E(i,a) for(auto (i)=(a).begin();(i)!=(a).end();++(i))
#define V vector
#define VI V<int>
#define VVI V<V<int>>
#define VL V<i64>
#define VVL V<V<i64>>
#define VD V<double>
#define VQ V<quad>
#define ALL(a) (a).begin(),(a).end()
#define VS V<string>
#define P pair
#define MP make_pair

#define DBG 0
#define PRINT 0
#define CHECK if(DBG==1) std::cout << "******* DEBUG IS ON *******" << std::endl;


string gf(const char* f, bool in){
	string file = "C:/gcj/";
#if DBG==1
	file+=FILE;
	if(in) file+=".txt";
	else file+="_out.txt";
#else
	if (in) file = file + f + ".txt";
	else file = file + f + "_out.txt";
#endif
	std::cout << "FILE " << file << endl;
	return file;
}

VS split(const string& s, char c){
	VS res;
	string tmp = "";
	F(i, s.size()){
		if (s[i] == c){
			if (tmp.size() > 0){
				res.push_back(tmp);
			}
			tmp.clear();
		}
		else {
			tmp += s[i];
		}
	}
	if (tmp.size() > 0){
		res.push_back(tmp);
	}
	return res;
}

void genf(const char* f, int n){
	ofstream fo(f);
	fo << n << '\n';
	for (int i = 0; i <= n; ++i){
		fo << i << '\n';
	}
	fo.flush();
	fo.close();
}




int main(int argc, char** argv){
	CHECK
	string currfile = "";
	currfile.append(*++argv);
	ifstream fi(("C:/gcj/" + currfile + ".txt").c_str());
	ofstream fo(("C:/gcj/" + currfile + "_out.txt").c_str());
	u64 T, N, x, Nx;
	fi >> T;
	F(i,T){
		fi >> N;
		if (N != 0){
			x = 1;
			int seen = 0;
			do {
				Nx = N * x;
				string s = to_string(Nx);
				F(j, s.size()){
					seen |= (1 << (s[j] - 48));
				}
				++x;
			} while (seen != ((1 << 10) - 1));
			fo << "Case #" << i + 1 << ": " << to_string(Nx) << '\n';
		}
		else {
			fo << "Case #" << i + 1 << ": " << "INSOMNIA"  << '\n';
		}
	}
	fo.flush();
	fo.close();
	fi.close();
	return 0;
}
