#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <list>
#include <map>
#include <set>

using namespace std;


int main(){
	
	string line;
	bool result;
  	ifstream myfile("small.in");
  	if(myfile.is_open()){
  		getline(myfile,line);
  		int test_cases = atoi(line.c_str());
  		//cout << "Test cases: " << test_cases << endl;
    	for(int i = 1; i <= test_cases; i++){
    		
    		result = true;
      		
      		cout << "Case #" << i << ": ";
      		
      		getline(myfile, line);
      		istringstream iss(line);
      		vector<string> tokens;
			copy(istream_iterator<string>(iss),
        	istream_iterator<string>(),
        	back_inserter<vector<string> >(tokens));
        	long long r, t;
        	
        	r = atoll(tokens[0].c_str());
        	t = atoll(tokens[1].c_str());
        	
        	long long i = (r+1)*(r+1) - r*r;
        	long long j = 0;
        	while((t -= i) >= 0){
        		i += 4;
        		j++;
        	}
      		
      		cout << j << endl;
      		
      		/*for(table::const_iterator cit = lawn.begin(); cit != lawn.end(); cit++){
      			for(row::const_iterator cjt = cit->begin(); cjt != cit->end(); cjt++)
      				cout << *cjt;
      			cout << endl;
      		}*/
      		
      		/*char res = result();
      		if(res == 'X' || res == 'O')
      			cout << "Case #" << i << ": " << res << " won" << endl;
      		else if(res == 'D')
      			cout << "Case #" << i << ": " << "Draw" << endl;
      		else if(res == 'N')
      			cout << "Case #" << i << ": " << "Game has not completed" << endl;*/
      			
      	
    	}
    	myfile.close();
  	}
  	else cout << "Unable to open file";
	
	return 0;
}
