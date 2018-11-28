#include <iostream>
#include <string.h>
using namespace std;
 
#define N  103
char s[N];

int main() {
	int tc,tst;
	cin >> tst;
	for(tc=1 ; tc<=tst ; ++tc)
	{
		cout << "Case #" << tc << ": ";

		int i, j=0, n = 0;
		cin >> s;

		char p, c = s[0];
		p = c;
		for(i=1 ; c ; ++i)
		{
			c = s[i];
			if(c!=p)
			{
				j = (p=='+');
				n++;
				p = c;
			}
		}

		cout << n-j << endl;
	}
	return 0;
}
