#include <iostream>
#include <string>

using namespace std;
using UInt = unsigned int;

int main()
{
	UInt N;
	cin >> N;
	for (UInt i = 0; i < N; ++i)
	{
		UInt K;
		string s;
		cin >> s >> K;
		UInt L(s.size());
		UInt count(0);
		UInt stop = (L-K)/2+1;
		for (UInt j = 0; j < stop; j++)
		{
			if (s[j] == '-')
			{
				s[j] = '+';
				for (UInt k = 1; k < K; ++k)
					s[j+k] = (s[j+k] == '-') ? '+' : '-';
				++count;
			}
			
			if (s[L-j-1] == '-')
			{
				s[L-j-1] = '+';
				for (UInt k = 1; k < K; ++k)
					s[L-j-1-k] = (s[L-j-1-k] == '-') ? '+' : '-';
				++count;
			}
		}
		
		bool OK(true);
		for (UInt j = 0; j < L; j++)
		{
			if (s[j] == '-')
			{
				cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
				OK = false;
				break;
			}
			
		}
		if (OK)
			cout << "Case #" << i+1 << ": " << count << endl;
	}
}


	

