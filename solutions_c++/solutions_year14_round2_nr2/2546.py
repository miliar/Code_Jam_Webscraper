#include <iostream>

using namespace std;

int main(void)
{
	int t;
	cin >> t;
	long long a,b,k;
	for(int qtd=1;qtd<=t;qtd++)
	{
		cout << "Case #" << qtd << ": ";
		int total=0;
		cin >> a >> b >> k;
		for(long long i=0;i<a;i++)
		{
			for(long long j=0;j<b;j++)
			{
				if((i&j)<k)
					total++;
			}
		}
		cout << total << endl;
	}
	return 0;
}
