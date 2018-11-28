#include <iostream>
#include <sstream>
#include <math.h>

using namespace std;

// utiliser comme ./speaktong < fin > fout

inline bool isPali(string & num)
{
	bool val = 1;
	int n = num.size();
	for(int i = 0; i <(n/2); i++)
	{
		if(num[i] != num[n-1-i])
			return 0;
	}
	return 1;
}

int main(int argc, char **argv)
{

(void)argc,(void)argv;

	ostringstream oss;
	string s;

	double result;
	
	int T; // number of test cases (lines of file)
	scanf("%d/n",&T);

	for(int i = 0; i < T; i++) // (tests)
	{
		result = 0;
		double Linf, Lsup;
		scanf("%lf %lf/n",&Linf,&Lsup);
		
		// raizes inteiras dentro do intervalo
		double Sinf = (double) ceil( sqrt(Linf) ); 
		double Ssup = (double) floor( sqrt(Lsup) ); 

		for(double i = Sinf; i <= Ssup; i++)
		{
			ostringstream oss0;
			oss0 << i;
			s = oss0.str();
			if(isPali(s))
			{
				double j = i*i;
				ostringstream oss1;
				oss1 << j;
				s = oss1.str();
				if(isPali(s))
					result++;
			}
		}
		
		cout.precision(1);
		cout << "Case #" << i+1 << ": " << result << endl;
		
	}
	return 0;
}


