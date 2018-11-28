#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include "BigIntegerLibrary.hh"//This library is in public domain. Download Link:https://mattmccutchen.net/bigint/bigint-2010.04.30.tar.bz2
using namespace std;
int getRoot(BigInteger a,BigInteger &mid){
		BigInteger right=a;
		BigInteger left=0;
		while(left <= right){
			mid=(left+right)/2;
			BigInteger estimate=mid*mid;
			if(estimate> a){
				right=mid-1;
			}
			else if(estimate<a){
				left=mid+1;
			}
			else return 1;
		}
		return 0;
}
int isPali(string s){
	int length=(int)s.size();
	for(int i=0;i <length/2;i++){
		if(s[i]!=s[length-1]){
			return 0;
		}
	}
	return 1;
}
string countFair(string A,string B){
		BigInteger count=0;
		BigInteger a=stringToBigInteger(A);
		BigInteger root=0;
		int result=getRoot(a,root);
		BigInteger start;
		if(result==1){
			start=root;
		}else{
			if(root*root < a){
				start=root+1;
			}
			else start=root;
		}
		BigInteger b=stringToBigInteger(B);
		BigInteger estimate=start*start;
		while(estimate <= b){
			string strEstimate=bigIntegerToString(estimate);
			string strStart=bigIntegerToString(start);
			if(isPali(strEstimate) && isPali(strStart)){count++;}
			start++;
			estimate=start*start;
		}
		return bigIntegerToString(count);	
}
using namespace std;
int main() {
	try {
			ifstream myfile;
			myfile.open("input.txt");
			if(myfile.is_open()){
				if(myfile.good()){
					string strN;int N;
					getline(myfile,strN);
					istringstream(strN) >> N;
					for(int test=1;test<=N;test++){
						string strAB,strA,strB;
						getline(myfile,strAB);
						istringstream abstream(strAB);
						getline(abstream,strA,' ');
						getline(abstream,strB,' ');
						cout << "Case #" << test << ": "<< countFair(strA,strB) << endl;
					}	
				}
			}
/*		BigInteger a; 
		int b = 535;
		a = b;
		b = a.toInt();
		BigInteger c(a); 
		BigInteger d(-314159265);
		BigInteger f = stringToBigInteger(s);
		std::string s2 = bigIntegerToString(f); 
		std::cout << f << std::endl;
		BigInteger g(314159), h(265);
		std::cout << (g + h) << '\n'
			<< (g - h) << '\n'
			<< (g * h) << '\n'
			<< (g / h) << '\n'
			<< (g % h) << std::endl;
		BigUnsigned i(0xFF0000FF), j(0x0000FFFF);
		std::cout.flags(std::ios::hex | std::ios::showbase);
		std::cout << (i & j) << '\n'
			<< (i | j) << '\n'
			<< (i ^ j) << '\n'
			<< (j << 21) << '\n'
			<< (j >> 10) << '\n';
		std::cout.flags(std::ios::dec);
		int maxPower = 10;
		BigUnsigned x(1), big314(314);
		for (int power = 0; power <= maxPower; power++) {
			std::cout << "314^" << power << " = " << x << std::endl;
			x *= big314; // A BigInteger assignment operator
		}
		std::cout << gcd(BigUnsigned(60), 72) << '\n'
			<< modinv(BigUnsigned(7), 11) << '\n'
			<< modexp(BigUnsigned(314), 159, 2653) << std::endl;
*/	} catch(char const* err) {
		std::cout << "The library threw an exception:\n"<< err << std::endl;
	}

	return 0;
}
