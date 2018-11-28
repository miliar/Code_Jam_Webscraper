#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	int i, j;
	unsigned long long int N, temp, k;

	for (i = 1; i <= T; i++)
	{
		cin >> N;
		cout << "Case #" << i << ": ";
		if (N == 0) {
			cout << "INSOMNIA" << endl;
			continue;
		}
		int dig[10] = {0};
		bool done = false;
		k = 2;
		temp = N;
		while(!done)
		{
			while (temp != 0)
			{
				dig[temp%10] = 1;
				temp = temp / 10;
			}
			done = true;
			for (j = 0; j <= 9; j++)
			{
				if (dig[j] == 0) done = false;
			}
			if (done) {
				cout << (k-1)*N << endl;
				break;
			}
			else 
				temp = (k++) * N;
		}
	}	
	return 0;
}
