#include <iostream>

using namespace std;
int Answer;
int N;
bool visited[10];
int visit_count;

int main()
{
	int T;

	cin >> T;

	for (int test_case = 1; test_case <= T; test_case++)
	{
		cin >> N;

		if (2 * N == N)
		{
			cout << "Case #" << test_case << ": ";
			cout << "INSOMNIA" << endl;
			continue;
		}

		for (int i = 0; i < 10; i++)
		{
			visited[i] = false;
		}

		visit_count = 0;
		Answer = 0;

		for (int i = 1;; i++)
		{
			int t = i * N;
			while (t)
			{
				int r = t % 10;
				t = t / 10;
				if (!visited[r])
				{
					visited[r] = true;
					visit_count++;
				}
			}

			if (visit_count == 10)
			{
				Answer = i * N;
				break;
			}

		}

		cout << "Case #" << test_case << ": ";
		cout << Answer << endl;
	}

	return 0;
}