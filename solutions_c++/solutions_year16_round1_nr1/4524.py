#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main(int argc, char const *argv[])
{
	std::ifstream infile("A-small-attempt0.in");
	short case_nbr=0;
	string str, final;
	infile >> str;
	while (infile >> str)
	{
		case_nbr++;
		final = str[0];
		for (char i = 1; i < str.length(); ++i)
		{
			if(str[i]>=final[0])
				final = str[i]+final;
			else
				final = final+str[i];
		}
    	cout<<"Case #"<<case_nbr<<": "<<final<<endl;
	}
	return 0;
}
