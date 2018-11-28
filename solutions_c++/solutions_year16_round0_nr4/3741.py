#include <iostream>
#include <fstream>
#include <stdio.h>
#define ll long long int
#define li long int

using namespace std;

int main()
{
	ifstream fin("input.in");
    ofstream fout("output.out");
	
	int t, l ;
	fin >> t;
	for(l = 1 ; l <= t ; l++)
	{
		int k, c, s, i;
		fin >> k >> c >> s;	
		if(c == 1)
		{
			if(s < k)
				fout << "Case #" << l << ": IMPOSSIBLE\n" ;
			else
			{
				fout << "Case #" << l << ": ";
				for(i = 1 ; i <= k ; i++)
				{
					fout << i << " ";	
				}	
				fout << endl;
			}	
		}
		else
		{
			if(s < k-1)
				fout << "Case #" << l << ": IMPOSSIBLE\n" ;
			else{
			
				if(k == 1)
					fout << "Case #" << l << ": 1\n";
				
				else
				{
					fout << "Case #" << l << ": " ;
					for(i = 2 ; i <= k ; i++)
					{
						fout << i << " ";
					}
					fout << endl;	
				}
				
			}
		}	
	}
}

