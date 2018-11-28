#include <iostream>
#include <string.h>
using namespace std;

#define L 1010 
char d[L], c[2*L];

int main() {
	int tc,tst;
	cin >> tst;
	for(tc=1 ; tc<=tst ; ++tc)
	{
		int i,n=0,ans=0;
		cin >> d;
		
		char *p = c+L;
		
		*p = d[0];

		for(i=1 ; d[i] ; ++i)
		{
			char cc = d[i];
			if(*p <= cc)
			{
				--p;
				*p = cc;
			}
			else
			{
				p[i] = cc;
			}
		}
		p[i] = 0;
		
		cout << "Case #" << tc << ": " << p << endl;


	}
	return 0;
}
