#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;


int main()
{
	int index=0;	
	int t;
	ifstream infile;
	infile.open("B-large.in", ios::in);

	ofstream outfile;
	outfile.open("B-large.out", ios::out);

	infile>>t;
	
	while(index++<t)
	{
		
	        char str[200];
		infile>>str;
		int i;		
	        long long aux[200];
	
		int len = strlen(str);
		
		if(str[0] == '-')
			aux[0] = 1;
		else
			aux[0] = 0;
		
		for(i = 1; i<len; i++)
		{
			if(str[i] == '+')
				aux[i] = aux[i-1];
			else
			{
				
				if(str[i-1] == str[i])
					aux[i] =aux[i-1];
				else
					aux[i] = 2 + aux[i-1];
			}
			
		}
		
		outfile<<"Case #"<<index<<": "<<aux[len-1]<<"\n";
			

	}
return 0;
}
