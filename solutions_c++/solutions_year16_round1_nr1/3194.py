#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <fstream>

int main(){
  std::ifstream in("A-large.in");
  int n;
  in >> n;
  std::string s;
  std::ofstream out("a-large.txt");
  for(int i = 0; i < n; ++i){
	in >> s;
	std::string answer;
	std::stringstream ss;
	for (char c : s){
		if( c < ss.str()[0]) ss << c;
		else{
		std::string s2 = ss.str();
		ss.str(std::string());
		ss << c << s2;
		}
	}
	out << "Case #" << i+1 << ": " << ss.str() << std::endl;
  }
}
