#include <map>
#include <string>
#include <iostream>
#include <fstream>
#include <bitset>
#include <cstdlib>
#define SMALL 0
#if (SMALL == 1)
#define INPUT "A-small-attempt2.in"
#define OUTPUT "A-small-attempt2.out"
#define SMAX 7
#else
#define INPUT "A-large.in"
#define OUTPUT "A-large.out"
#define SMAX 1000
#endif

int main(void)
{
	std::ifstream fi(INPUT);
	std::ofstream fo(OUTPUT);	
	int i, l, j, k, T, res, sum;
	char S[SMAX];
	fi >> T;
	i=0;
	if (fi.is_open())
	{
		while(i<T)
		{
			res = 0;
			fi >> k;
			fi >> S;
			for(l=0;l<=k;l++)
			{
				sum = 0;
				for(j=0;j<l;j++) 
				{
					sum += S[j] - '0';
				}			
				if((S[l])&&((sum+res) < l)) res += (l-sum-res);
			}
			i++;
			fo <<"Case #"<<i<<": "<<res<<"\n";
		}
		fi.close();
	}
	return 0;
}