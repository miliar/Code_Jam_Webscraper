#include <iostream> 
#include <string>
#include <cmath>
#include <sstream>
#include <fstream> 

using namespace std; 

string reverseS(string); 

int main() {
	ifstream input("C-small-attempt0.in"); 
	ofstream output("output-small.txt");
	unsigned long long tests;
	input >> tests;
	for(unsigned long long i = 1; i <= tests; i++) { 
		unsigned long long lowerlimit; 
		unsigned long long upperlimit;
		input >> lowerlimit; 
		input >> upperlimit; 
		unsigned long long l = ceil(sqrt((double)lowerlimit)); 
		unsigned long long u = ceil(sqrt((double)upperlimit));
		unsigned long long count = 0;
		for(unsigned long long i = l; i <= u; i++) {
			string s = static_cast<ostringstream*>( &(ostringstream() << i) )->str();
			if(reverseS(s) == s) {
				unsigned long long j = i*i; 
				string t = static_cast<ostringstream*>( &(ostringstream() << j) )->str();
				if(reverseS(t) == t) {
					if(lowerlimit <= j && upperlimit >= j) {
						count++;
					}
				}
			}
		}
		output << "Case #" << i << ": " << count << endl; 
	}
	return 0; 
}

string reverseS(string s) { 
	int length = s.length(); 
	if(length == 1) { 
		return s; 
	}
	string front = s.substr(0,length-1);
	string tail = s.substr(length-1,1);
	string reverse = tail.append(reverseS(front)); 
	return reverse; 
}