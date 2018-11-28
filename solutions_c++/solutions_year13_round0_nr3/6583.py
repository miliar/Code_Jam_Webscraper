#include "stdafx.h"
#include <iostream>
#include <fstream>
#include "string"
#include "cmath"
#include <stdio.h>

using namespace std;


void Reverse(string &theWord)
{       // Reverse the string contained in theWord.

       unsigned int i;
        char temp;
        
        for ( i=0; i<theWord.length()/2; i++)
        {
        	temp = theWord[i];
        	theWord[i] = theWord[theWord.length()-i-1];
        	theWord[theWord.length()-i-1] = temp;
        }
}  
int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("output.txt");
	int T;
	fin>>T;




	for (int test =0; test< T ; test++)
	{
		string S;
		fout<<"Case #"<<test+1<<": ";
		int A, B;
		int count=0;
		fin>>A>>B;

		int i = int (ceil (sqrt (A)));
		for ( ; i<= B ; i++)
		{

			    std::string s = std::to_string(i);
				Reverse(s);
				if ( i == atoi(s.c_str()))
				{
			
					int x = i*i;
					if ( x <= B)
					{
					    s = std::to_string(x);
						Reverse(s);
						if ( x == atoi(s.c_str()))
						{
							count++;
						}

					}
				}

		}

		fout<<count<<endl;
	}
	return 0;
}



