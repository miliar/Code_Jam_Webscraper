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
#define PRINT 0


int proc(ofstream& fo, const VI& v, bool split63){

	//well this is a cheesy solution 
	VI vp(v);
	make_heap(ALL(vp));
	int best = vp.front();
	int stop = vp.front()+1;
	int curr = best;
	int moves = 0;
	while(moves<=stop && vp.front()>1){
		int m = vp.front(),k;
		pop_heap(ALL(vp));
		vp.pop_back();
		if(split63 && m==9){
			m=6;
			k=3;
		}
		else {
			k = m/2;
			m -= k;
		}
		vp.push_back(m);
		push_heap(ALL(vp));
		vp.push_back(k);
		push_heap(ALL(vp));
		++moves;
		curr=moves+vp.front();
		if(best>curr) best=curr;
#if PRINT == 1
		fo << "curr = " << curr << " best = " << best << " moves = " << moves << endl;
		F(i,vp.size()){
			fo << vp[i] << " ";
		}
		fo << endl;
#endif 
	}
	return best;
}

void gen_file(int n){
	ofstream fo("C:/gcj/b2015.txt");
	fo << n + 1 <<endl;
	F(i,2){
		int p = 1000;
		fo << p << endl;
		F(j,p){
			fo << 1000 << " ";
		}
		fo << endl;
	}
	F(i,n){
		int p = (rand() % 1000)+1;
		fo << p << endl;
		F(j,p){
			fo << 1000 - (rand()%100) << " ";
		}
		fo << endl;
	}
	fo.flush();
	fo.close();
}

//B 2015
int main(int argc, char** argv){
	string fs;
#if DEBUG==1
	fs = "b2015";
	//gen_file(100);
	//return 0;
#else
	fs = *(++argv); 
#endif
	string infile = "C:/gcj/" + fs + ".txt";
	string outfile = "C:/gcj/" + fs + "_out.txt";
	ifstream fi(infile.c_str());
	ofstream fo(outfile.c_str());

	cout << "Running " << infile << endl;

	int t,p,n;
	fi >> t;
	F(i, t){
		fi >> n;
		VI v;
		F(j,n){
			fi >> p;
			v.push_back(p);
#if PRINT == 1
			fo << p << " ";
#endif
		}
#if PRINT == 1
			fo << endl;
#endif
		fo << "Case #" << i + 1 << ": " << min(proc(fo,v,true),proc(fo,v,false)) << endl;
		cout << "Case #" << i+1 << " complete" << endl;
#if PRINT == 1
			fo << endl << endl;
#endif
	}

	fo.flush();
	fo.close();
	fi.close();
	return 0;
}