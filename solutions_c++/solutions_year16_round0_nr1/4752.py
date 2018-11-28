#include <iostream>
#include<string.h>
using namespace std;


bool a[10];
void mark(unsigned long long N, int &marked)
{
	while (N)
	{
		short int lastdigit = N % 10;
		if (a[lastdigit] == false)
		{
			a[lastdigit] = true; marked++;
		}
		N /= 10;
	}
}

int main()
{	
#ifdef DEV_MODE 
	freopen("d://input_1.txt", "r", stdin);
#endif

	int T = 0; cin >> T;
	for (int t = 1; t <= T; t++)
	{
		int marked = 0;
		memset(a, 0, sizeof(a));
		unsigned long long N; cin >> N;

		unsigned long long N1 = 0;
		if (N)
		{
			while (marked < 10)
			{
				N1 += N;
				mark(N1, marked);
			}
		}

		if (N1 == 0)
			cout << "Case #" << t << ": " << "INSOMNIA" << endl;
		else
			cout << "Case #" << t << ": " << N1 << endl;
	}
	return 0;
}
