#include <iostream>
#include <string>
#include <stdlib.h>
#include <fstream>
#include <sstream>

int main(){
	std::ifstream ifs("/home/abidi/Bureau/A-large.in");
	std::string line;
	getline(ifs,line);
	std::ofstream ofs("/home/abidi/Bureau/A-large.out");
	int case_id=0;
	while(getline(ifs,line)){
		case_id++;
		std::istringstream is(line);
		int n;
		is>>n;
		std::string s;
		is>>s;
		int sum=0;
		int p=0;
		for(int i=0;i<n+1;i++){
			p+=std::max(i-sum,0);
			sum+=(int)(s[i]-'0')+std::max(i-sum,0);
		}
		ofs<<"Case #"<<case_id<<": "<<p<<std::endl;
	}
	return 0;
}
