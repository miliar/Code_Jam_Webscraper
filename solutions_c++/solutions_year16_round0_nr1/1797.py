#include <iostream>
#include <cstring>
using namespace std;

bool seen[10];
int cseen=0;

void process(unsigned long long int k)
{
	while(k>0)
	{
		if(!seen[k%10])
			cseen++;
		seen[k%10]=true;
		k/=10;
	}
}

int main()
{
	int T,n,x;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		cin >> n;
		cseen=0;
		memset(seen, 0, sizeof(seen));
		x=1;
		cout << "Case #" << t << ": ";
		process(x*n);
		if(n==0)
			cout << "INSOMNIA" << endl;
		else
		{
			while(cseen<10)
			{
				x++;
				process(x*n);
			}
			cout << x*n << endl;
		}
	}
	return 0;
}
