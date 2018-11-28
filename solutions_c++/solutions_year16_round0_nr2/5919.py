#include <iostream>
#include <string>
using namespace std;

int main()
{
	int i,T;
	cin >> T;
	string S;
	for (i = 1; i <= T; i++)
	{
		cin >> S;
		cout << "Case #" << i << ": ";
		
		int i;
		int n = S.length();
		int count = 0;
		char ans_temp=S[0];
		for (i = 1;i < n;i++)
		{
			if (S[i]!=S[i-1])
			{
				count ++;
				if (S[i-1] == '+') ans_temp = '-';
				if (S[i-1] == '-') ans_temp = '+';
			}
		}
		if (ans_temp == '-') count ++;
		cout << count << endl;
	}
}
