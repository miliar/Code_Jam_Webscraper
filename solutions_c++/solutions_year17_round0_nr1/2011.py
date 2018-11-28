#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++)
	{
		string S;
		int K;
		cin >> S >> K;
		
		int flips = 0;
		
		for (int i = 0; i <= S.size() - K; i++)
			if (S[i] == '-')
			{
				flips++;
				for (int j = i; j < i + K; j++)
					S[j] = (S[j] == '+' ? '-' : '+');
			}
		
		for (int i = S.size() - K + 1; i < S.size(); i++)
			if (S[i] == '-')
				flips = -1;
		
		 cout << "Case #" << t << ": " << (flips >= 0 ? to_string(flips) : "IMPOSSIBLE") << "\n";
	}
	
	return 0;
}

