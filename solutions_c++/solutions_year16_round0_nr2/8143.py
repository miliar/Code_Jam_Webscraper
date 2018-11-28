#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>

using namespace std;


bool happy(string str){
	for(int i=0;i<str.length();i++)
	{
		if(str[i]!='+')
            return false;
	}
	return true;
}

int main()
{
	int t;

	std::fstream infile("C:\\Users\\Siddharth\\Desktop\\ProblemBsmallinput.txt", std::ios_base::in);

    ofstream outfile("C:\\Users\\Siddharth\\Desktop\\ProblemBsmalloutput.txt", std::ios_base::out);

    infile>>t;

	for(int c_no = 1;c_no <=t ; c_no++)
	{

		string sequence;
		infile>>sequence;
		int output = 0;

		for(int i = sequence.length() - 1; i >= 0; i--)
		{

			if(happy(sequence))
                break;
			if(sequence[i]=='-')
			{
				for(int j=0;j<=i;j++)
				{
					if(sequence[j]=='-')
						sequence[j]='+';
					else
						sequence[j]='-';
				}
				output++;
			}
		}
		outfile<<"Case #"<<c_no<<": "<<output<<"\n";
	}
}
