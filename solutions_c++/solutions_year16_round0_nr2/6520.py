#include <iostream>

using namespace std;
int Answer;
char input[100];
int length;

int main()
{
	int T;
	char c;

	scanf("%d\n", &T);

	for (int test_case = 1; test_case <= T; test_case++)
	{
		length = 0;

		scanf("%c", &c);

		while (c != '\n')
		{
			input[length++] = c;
			scanf("%c", &c);
		}

		Answer = 0;

		int i = -1;
		int count = 0;

		while (i < length-1)
		{
			if (count)
				Answer++;

			count = 0;
			while (i+1 < length && input[i + 1] == '-')
			{
				i++;
				count++;
			}

			if (count)
				Answer++;

			while (i + 1 < length && input[i + 1] == '+')
			{
				i++;
				count++;
			}
		}

		cout << "Case #" << test_case << ": ";
		cout << Answer << endl;
	}

	return 0;
}