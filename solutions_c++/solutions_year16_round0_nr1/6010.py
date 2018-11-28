#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		long N;
		cin >> N;
		if (N == 0)
		{
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		
		int matchDigits = 0;
		int match[10] = {0};
		
		int m = 0;
		while (matchDigits != 10)
		{
			m++;
			long p = m * N;
			while(p != 0)
			{
				int digit  =  p % 10;
				matchDigits = matchDigits - match[digit] + 1;
				match[digit] = 1;
				p = p / 10;
			}
		
		}
		cout << "Case #" << i + 1 << ": " << m * N <<  endl;		
	}
}
