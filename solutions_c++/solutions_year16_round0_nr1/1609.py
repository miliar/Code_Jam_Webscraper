// Sheep

#include <iostream>
#include <string.h>
using namespace std;
 
char d[10];

int main() {
	int tc,tst,mx=0;
	cin >> tst;
	for(tc=1 ; tc<=tst ; ++tc)
	{
		int i,nn,c=0;
		long long n;
		cin >> nn;
		n = nn;
		cout << "Case #" << tc << ": ";
		if(n==0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}
		memset(d,0,sizeof(d));
		
		for(i=1 ; i<=1000000 ; ++i)
		{
			long long j = i*n;
			while(j)
			{
				int jj = j%10;
				j /= 10;
				if(!d[jj])
				{
					d[jj] = 1;
					c++;
					if(c == 10)
					{
						cout << i*n << endl;
						if(mx < i)
							mx = i;
						goto NEXT;
					}
				}
			}
		}
		cout << "INSOMNIA" << endl;
NEXT:
		;
	}
	cout << "mx = " << mx << endl;
	return 0;
}
