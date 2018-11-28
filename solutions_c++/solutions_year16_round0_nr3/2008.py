#if __cplusplus < 201103L
#error it should be c++11
#endif

#include <boost/multiprecision/cpp_int.hpp>
//#include <boost/math/special_functions/prime.hpp>
//#include <boost/multiprecision/miller_rabin.hpp>
#include <iostream>
#include <iomanip>

#include <fstream>
#include <string>
#include <vector>
#include <array>
#include <bitset>

using namespace std;
using namespace boost::multiprecision;
bool DEBUGFLAG=false;
typedef int128_t numtype;
//typedef unsigned long long numtype;


vector<numtype> primelist={2,3,5,7,11,13,17,19,23,29};
array<numtype,8> prime30={1,7,11,13,17,19,23,29};

bool prime(numtype threshold);
numtype basing (int base, numtype bin_base);
int testcase(ofstream& op, size_t length, size_t casesize);
numtype prime_efftest(numtype test);

int main(int argc, char **argv){
	string filename;
	for (int i = 1; i < argc; ++i)
		if (string("--debug").compare(argv[i])==0) DEBUGFLAG=true;
		else filename = string(argv[i]);
	ifstream ip(argv[1]);
	ofstream op("output.txt");
	size_t T,N,J;
	ip >> T>>N>>J;
	op << "Case #1:"<<endl;
	testcase(op,N,J);
	op.close();
	ip.close();
	return 0;
}

int testcase(ofstream& op, size_t length, size_t casesize){
	int base;
	size_t cnt=0;
	numtype factor[11];
	for (numtype num= (1<<(length-1))+1; num <= (1<<length) -1; num+=2){
		for (base =2; base<=10; ++base){
			factor[base]=prime_efftest(basing(base,num));
			if(factor[base]==0) break;
		}
		if (base==11) {
			op << static_cast<bitset<32>>(num) << " ";
			for (size_t j = 2; j <= 10; ++j)
				op << factor[j] << " ";
			op << endl;
			if (++cnt >= casesize) return 0;
		}//else op << static_cast<bitset<16>>(num) << basing(3,num) <<endl;
	}
}

numtype basing (int base, numtype bin_base){
	numtype result = 0;
	numtype factor = 1;
	for (; bin_base>0; bin_base >>=1, factor *=base)
		if (bin_base & 1) result += factor;
	return result;
}

bool prime(numtype threshold){
	bool flag=false;
	numtype subject;
	bool result=false;
	for (numtype i = (primelist.back()/30); i*30 < threshold; ++i){
		for (int j=0; j<8; ++j){
			flag=false;
			subject = (30*i+prime30[j]);
			if (subject <= primelist.back()) continue;
			for (int k = 0; k < primelist.size(); ++k){
				if (subject%primelist[k]==0){
					flag=true;
					break;
				}
			}
			if (flag==false) primelist.push_back(subject);
			if (subject==threshold) result = !flag;
		}
	}
	return result;
}

numtype prime_efftest(numtype test){
	size_t lastsize = 0;
	numtype result = 0;
	for (numtype i = primelist.back(); i <= test/2; prime(i+=1000)){
		for (size_t j = lastsize; j < primelist.size(); ++j)
			if (test%primelist[j]==0) return primelist[j];
		lastsize = primelist.size();
	}
	return 0;
}

