#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <bitset>
using namespace std;

std::bitset<10> bitvec;
std::bitset<10> checkvec;
unsigned solve_problem (unsigned long long num) {
	unsigned i=1;
	unsigned long long orig=num;
	while (1) {
		unsigned long long n=orig;
		while (n > 0) {
			unsigned rem = n%10;
			bitvec.set(rem);
			if (bitvec == checkvec)
				return orig;
			n =n/10;
		}
		++i;
		orig = num*i;
	}
	return 0;
}
int main(int argc, char* argv[])
{
	checkvec.flip();
  string filename= argv[1];
  ifstream file(filename.c_str());
	int numTests;
	file>>numTests;
	string line;
	unsigned x=1;
  while (file) {
		getline (file, line);
    if(!line.empty()){
      string buf;
			unsigned long long num;
      stringstream ss(line);
      ss >> buf;
			num = atof(buf.c_str());
			if (num ==0)
				cout <<"Case #"<<x<<": INSOMNIA"<<std::endl;
			else { 
				cout <<"Case #"<<x<<": "<<solve_problem(num)<<std::endl;
				bitvec.reset();
			}
			++x;
		}
	}
  file.close();
}
