#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t=1; t<=T; t++)
	{
		int solution = 0;
		string S;
		cin >> S;
		if (S[0] == '-')
			solution++;
		for (unsigned i=1; i<S.size(); i++)
			if (S[i-1] == '+' && S[i] == '-')
				solution += 2;
		cout << "Case #" << t << ": " << solution << endl;
	}
	return 0;
}
