#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <iterator>
#include <fstream>
#include <math.h>
#include <sstream>
typedef unsigned long uint64_t;
using namespace std;
int is_palindrome(uint64_t num)
{
	uint64_t  temp=num;
	uint64_t sum=0;
	uint64_t r = 0;
	while(temp){
		r=temp%10;
		temp=temp/10;
		sum=sum*10+r;
	}
	if(num == sum)
		return 1;
	return 0;
}

int caseno = 1;
void run_test(uint64_t l, uint64_t h)
{
	int t = 0;
	for(uint64_t i = l ; i <= h; i++)
	{
	   if(is_palindrome(i) )
		{
			double d_sq = sqrt(i);
			uint64_t sq = d_sq;
			if(sq == d_sq)
			if(is_palindrome(sq))
			 t++;
		}
	}
	cout<<"Case #"<<caseno<<": "<<t<<endl;
	caseno ++;
}

inline std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while(std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}


inline std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    return split(s, delim, elems);
}

int main(int argc,char ** argv)
{
  const char *file = argv[1];
  int total_test_cases = 0;
  ifstream in_stream;
  in_stream.open(file);
  string line;
  std::getline(in_stream, line);
  total_test_cases = atoi(line.c_str());
  while(std::getline(in_stream, line))
  {
	std::vector<std::string> tokens = split(line, ' ');
	run_test(atol(tokens[0].c_str()), atol(tokens[1].c_str()));
  }

 return 0;
}
