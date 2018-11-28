#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <iterator>
#include <cmath>

using namespace std;

bool is_palindrome(int a){
	
	std::stringstream ss;
    ss << a;
    std::string s(ss.str());
	
	if(equal(s.begin(), s.begin() + s.size()/2, s.rbegin()))
		return true;
	return false;
	
}

int main(){
	
	long long start, end, max_pal, num_pals;
	string line;
  	ifstream myfile("small.in");
  	if(myfile.is_open()){
  		getline(myfile,line);
  		int test_cases = atoi(line.c_str());
    	for(int i = 1; i <= test_cases; i++){
      		
      		num_pals = 0;
      		getline(myfile,line);
      		istringstream iss(line);
      		vector<string> tokens;
			copy(istream_iterator<string>(iss),
        	istream_iterator<string>(),
        	back_inserter<vector<string> >(tokens));
        	
        	start = atoll(tokens[0].c_str());
        	end = atoll(tokens[1].c_str());
        	
        	max_pal = floor(sqrt(end));
      		      		
      		for(int j = 1; j <= max_pal; j++){
      			if(is_palindrome(j) && is_palindrome(j*j) && j*j >= start)
      				num_pals++;
      		}
      		cout << "Case #" << i << ": " << num_pals << endl;
      		
    	}
    	myfile.close();
  	}
  	else cout << "Unable to open file";
	
	return 0;
}
