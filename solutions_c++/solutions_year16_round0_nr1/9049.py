#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <bitset>
#include <fstream>
using namespace std;




int main(int argc, char *argv[])
{
	ofstream ecrire("output.txt");
	ifstream lire("input.txt");
	long long K;
	lire >> K;
	for(long long k=0; k < K;k++)
	{
		long long N,n;
		lire >> n; 
		N=n;
		ecrire<<"Case #"<<k+1<<": ";
		if(N <=  0)
			ecrire<<"INSOMNIA\n";
		else
		{
			bitset<10> test(0);	
			for(size_t i = 1 ; true ; i++)
			{
			    string  n_inString = to_string(N);
				for(size_t j = 0 ; j <  n_inString.size() ;j++)
				{
					test[9-(n_inString[j]-'0')]=1;
				}
				
				if(test.all()) 
				{
					ecrire<<N<<endl;
					break;
				}
				N = i*n;
				
			}
		}
	}
}