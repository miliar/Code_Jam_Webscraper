#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <sstream>
#include <fstream>

using namespace std;

int main()
{

	int t;
    string temp;

     std::fstream infile("C:\\Users\\Siddharth\\Desktop\\ProblemAsmallinput.txt", std::ios_base::in);

    ofstream outfile("C:\\Users\\Siddharth\\Desktop\\ProblemAsmalloutput.txt", std::ios_base::out);

    infile>>t;
    for(int i = 0; i < t; i++)
    {

        int n;
        infile>>n;

        if(n == 0)
        {
            outfile << "Case #" << i+1 << ": INSOMNIA\n";
        }
        else
        {
            int multiplier = 1;
            long long int number = n;
			std::string total;

            while (total.size() < 10)
            {
            	number =n* multiplier;
                std::stringstream ss;
                ss << number;
                std::string s ;
                s.append(ss.str());

	   		    std::sort( s.begin(), s.end() );
			    s.erase( std::unique( s.begin(), s.end() ), s.end() );

                total = total + s;
                std::sort( total.begin(), total.end() );
                total.erase( std::unique( total.begin(), total.end() ), total.end() );

                ++multiplier;
            }

            outfile << "Case #" << i+1 << ": "<< number << "\n";

        }



    }
	return 0;
}
