/*
Author: Ayoub Serti
CodeJam 2015
Problem A Standing Ovation
*/

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main()
{
	int T, Smax,i =0;
	string Shy;

	ifstream fin;
	ofstream fout;

	fin.open("A.in",ifstream::in);
	fout.open("A.out",ofstream::out);

	fin >> T ;
	
	while(T)
	{
		i++;
		fin >> Smax;
		fin >> Shy;
		//int* s = (int*)::malloc(Smax*sizeof(int));
		
		size_t sz = Shy.size();
		size_t Seff = Smax;
		int result = 0;
		size_t cumul =0;
		for ( size_t j =0;j<sz-1  ; ++j )
		{
			int valJ = Shy[j] - '0';
			/*if ( Shy[j] == '0' )
			{
			 result++;
			 Seff--;
			}*/
			cumul+=valJ;
			if ( cumul < j+1 && (Shy[j+1] - '0'>0   ))
			{
				size_t ajout = j+1 - cumul;
				result+=ajout;
				cumul+=ajout;
			}
			
		}
		
		fout << "Case #" << i << ": " << result << endl;
		T--;
	}
	

	return 0;
}