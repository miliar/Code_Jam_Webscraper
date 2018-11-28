#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[])
{
	std::ifstream infile("A-large.in");
	short case_nbr=0;
	int n, multiplier, value, current_length;
	ostringstream ss;
	string str;
	string digits;
	char digit,i;
	infile >> n;
	while (infile >> n)
	{
		case_nbr++;
		if(n == 0){
			cout<<"Case #"<<case_nbr<<": "<<"INSOMNIA"<<endl;
			continue;
		}
    	multiplier = 1;
    	digits = "0123456789";
    	while(digits.length()){
    		value = n*multiplier;
	    	i = 0;
			ss << value;
			str = ss.str();
			
			while(i<str.length())
			{
				digit = str.at(i);
				// Removing current character from current string
				current_length == str.length();
				str.erase(std::remove(str.begin(), str.end(), digit), str.end());
				// Removing current character from digits string
				digits.erase(std::remove(digits.begin(), digits.end(), digit), digits.end());
				// Icrement position only if a character has been removed
				if(str.length() == current_length)
					i++;
			}
			multiplier++;
    	}
    	cout<<"Case #"<<case_nbr<<": "<<value<<endl;
    	ss.str(string());
	}
	return 0;
}
