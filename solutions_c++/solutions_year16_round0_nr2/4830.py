#include <iostream>
#include<string.h>
using namespace std;

char S[101];
int main()
{	
#ifdef DEV_MODE 
	freopen("d://input_1.txt", "r", stdin);
#endif
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		cin >> S;

		int len = strlen(S);

		char lastch = '+'; int count = 0;
		for (int i = len - 1; i >= 0; i--)
		{
			if (lastch != S[i])
			{
				count++; lastch = S[i];
			}
		}

		cout << "Case #" << t << ": " << count<<endl;
	}

	return 0;
}
