#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <stack>
#include <map>
using namespace std;
map<string, char> numbers;
string recursion(map<char, int> digits, string output){
//cout << output << endl;
	    for (auto const& number : numbers)
		{
		
		bool possible = true;
		
		map<char, int> temp = digits;
		for(char e : number.first){			
			if(temp.count(e) ==0 || temp[e] <= 0){
				possible = false;
				break;
			}
			temp[e]-=1;			
		}
		if(possible){
			string opl = recursion(temp, output+number.second);
			if(opl != "")
				return opl;
		}	
		temp = digits;
			
		bool done =true;
		for(auto const& x : temp){
		if(x.second != 0){
			done = false;
			break;
		}
		}
		
		if(done)
			return output;
		
	}
	
	return "";
}

int main()
{	
	numbers["ZERO"] = '0';
	numbers["ONE"] = '1';
	numbers["TWO"] = '2';
	numbers["THREE"] = '3';
	numbers["FOUR"] = '4';
	numbers["FIVE"] = '5';
	numbers["SIX"] = '6';
	numbers["SEVEN"] = '7';
	numbers["EIGHT"] = '8';
	numbers["NINE"] = '9';

	int T;
    scanf("%d\n", &T);
    for(int testCase=0; testCase<T; testCase++){
        map<char, int> digits;
        string line;
        getline (cin,line);
        for(int i=0; i<line.size(); i++){
        	if(digits.count(line[i])>0)
        		digits[line[i]] += 1;
        	else
        		digits[line[i]] = 1;
        }
   		//cout << digits['O'] << endl;
   		
	
	string output = recursion(digits, "");
	sort(output.begin(), output.end());
	cout << "Case #" << testCase+1 << ": " << output << endl;
        //printf("Case #%d: %d\n",testCase+1, oplossing);
    }
    return 0;
}

