#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
using namespace std;

int main(int argc, char const *argv[])
{
	std::ifstream infile("B-large.in");
	short case_nbr=0, switches;
	string str;
	infile >> str;
	bool all_plus;
	while (infile >> str)
	{
		switches = 0;
		all_plus = false;
		case_nbr++;
		while(!all_plus){
			all_plus = true;
			for(short i = str.length() -1; i>=0;i--){
				if (str.at(i) == '-')
				{
					for(short j = 0; j <=i; j++){
						if (str.at(j) == '-')
							str[j] = '+';
						else
							str[j] = '-';
					}
					all_plus =false;
					switches++;
					break;
				}
			}
		}
    	cout<<"Case #"<<case_nbr<<": "<<switches<<endl;
	}
	return 0;
}
