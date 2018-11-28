#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");
	
	int t;
	fin >> t;
		
	for(int tnum = 1; tnum <= t; ++tnum)
		{
			int smax;
	  	string shyness;
			fin >> smax >> shyness;
			int standing = shyness[0] - '0';			
			int ans = 0;
			for(int i = 1; i <= smax; ++i)
				{
					if(standing < i)
						{	
							ans += (i - standing);		
							standing += (i - standing);
						}
					standing += (shyness[i] - '0');		 
				}
			fout << "Case #" << tnum << ": " << ans << endl; 		
		}	
	return 0;
}
