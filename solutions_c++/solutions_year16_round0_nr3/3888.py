#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <cassert>
#include "math.h"
#include <cstdlib>

using namespace std;

map <string, vector<unsigned long long> > results;
 
string addBitStrings( string first, string second );
 
// Helper method: given two unequal sized bit strings, converts them to
// same length by aadding leading 0s in the smaller string. Returns the
// the new length
int makeEqualLength(string &str1, string &str2)
{
    int len1 = str1.size();
    int len2 = str2.size();
    if (len1 < len2)
    {
        for (int i = 0 ; i < len2 - len1 ; i++)
            str1 = '0' + str1;
        return len2;
    }
    else if (len1 > len2)
    {
        for (int i = 0 ; i < len1 - len2 ; i++)
            str2 = '0' + str2;
    }
    return len1; // If len1 >= len2
}

// code borrowed from geeks for geeks C++
string addBitStrings( string first, string second )
{
    string result;  // To store the sum bits
 
    // make the lengths same before adding
    int length = makeEqualLength(first, second);
 
    int carry = 0;  // Initialize carry
 
    // Add all bits one by one
    for (int i = length-1 ; i >= 0 ; i--)
    {
        int firstBit = first.at(i) - '0';
        int secondBit = second.at(i) - '0';
 
        // boolean expression for sum of 3 bits
        int sum = (firstBit ^ secondBit ^ carry)+'0';
 
        result = (char)sum + result;
 
        // boolean expression for 3-bit addition
        carry = (firstBit & secondBit) | (secondBit & carry) | (firstBit & carry);
    }
 
    // if overflow, then add a leading 1
    if (carry)
        result = '1' + result;
 
    return result;
}
void checkIfNonTrivial (vector <unsigned long long> &result, std::string  &bitVec) {
	
	//cout <<bitVec<<endl;
	int divisors [9] = {3, 7, 5, 6, 31, 8, 27, 5, 77};	
	for (int base =2; base <=10; ++base) {
		unsigned long long value = 0;
		for(int i=0; i<bitVec.size(); ++i){
			int v1 = 0;
			if (bitVec[i] == '1')
				v1 =1;
			else 
				v1=0;
			value += v1*pow(base, (bitVec.size()-1-i));
		}
		
		//for (unsigned long long m=2; m <10000000; ++m){
			unsigned m = divisors[base-2];
			if (value%m ==0) {
				//unsigned long long quotient = value/m;
				//if(quotient%2 ==0 ) {
					result.push_back(m);
					//break;
				//}
			//} 
		}	
	}
}
	  
void recurse_on_bitvec ( std::bitset <10> &bitvec, int pos) {
		if (pos >0 ) {
			bitvec.reset(pos);
			recurse_on_bitvec(bitvec, pos-1);
			bitvec.set(pos);
			recurse_on_bitvec(bitvec, pos-1);		
		} else { 
			string mult = "000";
			string s1 = '1' + bitvec.reset(0).to_string()+ '1' + mult;
			string s2 = '1'+ bitvec.reset(0).to_string() + '1';
			string result = addBitStrings(s1,s2);
			//cout <<s1<<" "<<s2<<" "<<result<<endl;
			vector <unsigned long long> v1;
			if (result.size() ==16 && results.size() <50)
				checkIfNonTrivial (v1, result);
			//cout <<result<<" "<<v1.size()<<endl;
			if (v1.size() ==9 && results.size() <50) { 
				results.insert(make_pair(result, v1));
				//cout <<result<<endl;
			}
			
			s1 = '1' + bitvec.set(0).to_string() + '1' + mult;
			s2 = '1'+ bitvec.set(0).to_string() + '1';
			//cout <<s1<<" "<<s2<<" "<<result<<endl;
			result = addBitStrings(s1,s2);
			v1.clear();
			if (result.size() ==16 && results.size() <50)
				checkIfNonTrivial (v1, result);
			if (v1.size() ==9 && results.size() <50) { 
				results.insert(make_pair(result, v1));
				//cout <<result<<endl;
			}
			return;
		}
}
	
int main(int argc, char* argv[])
{
	std::bitset<10> bitvec;
	cout << "Case #1:"<<endl;
	int pos = 9;
	recurse_on_bitvec(bitvec,pos);
	unsigned count =0;
	
	for (auto& kv : results) {
		if(kv.first.size() ==16 && count <50) { 
			cout << kv.first<<" " ;
			for (auto& it : kv.second) 
				cout<< it<<" ";
			cout<<endl;
			++count;
		}
	}
	return 0;
}
