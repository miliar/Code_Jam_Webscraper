#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T, N, result, current = 0;
	string S;

	cin >> T;
	for(int i=0; i<T; i++)
	{
		result = 0; 
		current = 0;

		cin >> N;
		cin >> S;

		for(int j=1; j<N+1; j++)
		{
			current += (S[j-1]-48);
			if(j-current > 0)
			{
				result += (j-current);
				current += (j-current);
			}
		}
		cout << "Case #" << i+1 << ": " << result << endl;
	}


	return 0;
}
